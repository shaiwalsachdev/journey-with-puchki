package com.shaix2.journey;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.Context;
import android.graphics.Color;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Build;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.CookieManager;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceError;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends Activity {

    // Remote Live Production URL hosted on Render
    public static final String APP_URL = "https://journey-with-puchki.onrender.com/";

    private WebView mWebView;
    private ProgressBar mProgressBar;
    private FrameLayout mErrorLayout;
    private TextView mErrorText;
    private long mLastBackPressTime = 0;

    @Override
    @SuppressLint("SetJavaScriptEnabled")
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Keep screen awake for slideshows and background playback
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);

        // Fullscreen edge-to-edge layout
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        setupFullScreen();

        // Build root layout
        FrameLayout rootLayout = new FrameLayout(this);
        rootLayout.setBackgroundColor(Color.parseColor("#0f0c1b"));

        // Setup WebView
        mWebView = new WebView(this);
        mWebView.setLayoutParams(new FrameLayout.LayoutParams(
                FrameLayout.LayoutParams.MATCH_PARENT,
                FrameLayout.LayoutParams.MATCH_PARENT));
        mWebView.setBackgroundColor(Color.parseColor("#0f0c1b"));

        // Enable D-Pad remote focus on the webview for Android TV
        mWebView.setFocusable(true);
        mWebView.setFocusableInTouchMode(true);
        mWebView.requestFocus();

        configureWebSettings();

        // Progress bar for sleek loading indication
        mProgressBar = new ProgressBar(this, null, android.R.attr.progressBarStyleHorizontal);
        FrameLayout.LayoutParams pbParams = new FrameLayout.LayoutParams(
                FrameLayout.LayoutParams.MATCH_PARENT, 8);
        mProgressBar.setLayoutParams(pbParams);
        mProgressBar.setMax(100);
        mProgressBar.setProgress(0);

        // Offline / Error screen overlay
        mErrorLayout = createErrorLayout();

        rootLayout.addView(mWebView);
        rootLayout.addView(mProgressBar);
        rootLayout.addView(mErrorLayout);
        setContentView(rootLayout);

        // Attach clients and load remote app
        setupWebClients();
        loadApp();
    }

    private void setupFullScreen() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
            View decorView = getWindow().getDecorView();
            decorView.setSystemUiVisibility(
                    View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                            | View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                            | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                            | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                            | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                            | View.SYSTEM_UI_FLAG_FULLSCREEN);
        }
    }

    @SuppressLint("SetJavaScriptEnabled")
    private void configureWebSettings() {
        WebSettings settings = mWebView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setDatabaseEnabled(true);
        settings.setMediaPlaybackRequiresUserGesture(false); // Enable auto-play music & slideshow
        settings.setAllowFileAccess(true);
        settings.setAllowContentAccess(true);
        settings.setLoadsImagesAutomatically(true);
        settings.setUseWideViewPort(true);
        settings.setLoadWithOverviewMode(true);
        settings.setSupportZoom(false);
        settings.setBuiltInZoomControls(false);

        // Performance & caching
        settings.setCacheMode(WebSettings.LOAD_DEFAULT);

        // Custom User Agent identifier so backend and TV CSS know when app is running in TV/Android shell
        String customUA = settings.getUserAgentString() + " PuchkiMobileApp/1.0 (" + (isTv() ? "AndroidTV" : "AndroidMobile") + ")";
        settings.setUserAgentString(customUA);

        CookieManager.getInstance().setAcceptCookie(true);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            CookieManager.getInstance().setAcceptThirdPartyCookies(mWebView, true);
        }
    }

    private boolean isTv() {
        android.app.UiModeManager uiModeManager = (android.app.UiModeManager) getSystemService(UI_MODE_SERVICE);
        return uiModeManager != null && uiModeManager.getCurrentModeType() == android.content.res.Configuration.UI_MODE_TYPE_TELEVISION;
    }

    private void setupWebClients() {
        mWebView.setWebChromeClient(new WebChromeClient() {
            @Override
            public void onProgressChanged(WebView view, int newProgress) {
                if (newProgress < 100) {
                    mProgressBar.setVisibility(View.VISIBLE);
                    mProgressBar.setProgress(newProgress);
                } else {
                    mProgressBar.setVisibility(View.GONE);
                }
            }
        });

        mWebView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                // Keep all internal navigation inside this webview
                view.loadUrl(request.getUrl().toString());
                return true;
            }

            @Override
            public void onPageFinished(WebView view, String url) {
                super.onPageFinished(view, url);
                mErrorLayout.setVisibility(View.GONE);
                // Inject spatial navigation helper & TV CSS if on TV
                injectTvNavigationHelpers();
            }

            @Override
            public void onReceivedError(WebView view, WebResourceRequest request, WebResourceError error) {
                super.onReceivedError(view, request, error);
                if (request.isForMainFrame()) {
                    showError("Could not reach Journey with Puchki. Please check your internet connection.");
                }
            }
        });
    }

    private void injectTvNavigationHelpers() {
        // Injects TV remote focus highlights and D-Pad listeners into the rendered webpage
        String js = "(function() {" +
                "  if (window.__tvInjected) return;" +
                "  window.__tvInjected = true;" +
                "  var style = document.createElement('style');" +
                "  style.innerHTML = `" +
                "    :focus, :focus-visible, .tv-focused {" +
                "      outline: 4px solid #ff4d8d !important;" +
                "      box-shadow: 0 0 20px rgba(255, 77, 141, 0.8) !important;" +
                "      transform: scale(1.04);" +
                "      transition: transform 0.15s ease, box-shadow 0.15s ease !important;" +
                "    }" +
                "  `;" +
                "  document.head.appendChild(style);" +
                "})();";
        mWebView.evaluateJavascript(js, null);
    }

    private void loadApp() {
        if (isNetworkAvailable()) {
            mErrorLayout.setVisibility(View.GONE);
            mWebView.loadUrl(APP_URL);
        } else {
            showError("No internet connection detected.\nPlease connect to Wi-Fi and tap retry.");
        }
    }

    private boolean isNetworkAvailable() {
        ConnectivityManager cm = (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
        if (cm == null) return false;
        NetworkInfo info = cm.getActiveNetworkInfo();
        return info != null && info.isConnected();
    }

    private FrameLayout createErrorLayout() {
        FrameLayout layout = new FrameLayout(this);
        layout.setBackgroundColor(Color.parseColor("#0f0c1b"));
        layout.setVisibility(View.GONE);

        android.widget.LinearLayout content = new android.widget.LinearLayout(this);
        content.setOrientation(android.widget.LinearLayout.VERTICAL);
        content.setGravity(android.view.Gravity.CENTER);
        FrameLayout.LayoutParams cParams = new FrameLayout.LayoutParams(
                FrameLayout.LayoutParams.WRAP_CONTENT,
                FrameLayout.LayoutParams.WRAP_CONTENT,
                android.view.Gravity.CENTER);
        content.setLayoutParams(cParams);

        mErrorText = new TextView(this);
        mErrorText.setTextColor(Color.WHITE);
        mErrorText.setTextSize(18);
        mErrorText.setGravity(android.view.Gravity.CENTER);
        mErrorText.setPadding(40, 20, 40, 40);
        content.addView(mErrorText);

        android.widget.Button retryBtn = new android.widget.Button(this);
        retryBtn.setText("Retry Connection");
        retryBtn.setBackgroundColor(Color.parseColor("#ff4d8d"));
        retryBtn.setTextColor(Color.WHITE);
        retryBtn.setPadding(30, 15, 30, 15);
        retryBtn.setFocusable(true);
        retryBtn.setOnClickListener(v -> loadApp());
        content.addView(retryBtn);

        layout.addView(content);
        return layout;
    }

    private void showError(String msg) {
        if (mErrorText != null) {
            mErrorText.setText(msg);
        }
        if (mErrorLayout != null) {
            mErrorLayout.setVisibility(View.VISIBLE);
        }
    }

    // Android TV remote and Phone Back button handler
    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if (keyCode == KeyEvent.KEYCODE_BACK) {
            if (mWebView != null && mWebView.canGoBack()) {
                mWebView.goBack();
                return true;
            }
            // Double tap to exit to prevent accidental closing on phone or TV
            if (System.currentTimeMillis() - mLastBackPressTime < 2000) {
                finish();
            } else {
                mLastBackPressTime = System.currentTimeMillis();
                Toast.makeText(this, "Press back again to exit Puchki Journey", Toast.LENGTH_SHORT).show();
            }
            return true;
        }

        // TV Remote Play/Pause and Media Keys support
        if (keyCode == KeyEvent.KEYCODE_MEDIA_PLAY_PAUSE || keyCode == KeyEvent.KEYCODE_MEDIA_PLAY) {
            mWebView.evaluateJavascript("if (typeof toggleMusic === 'function') toggleMusic();", null);
            return true;
        }

        return super.onKeyDown(keyCode, event);
    }

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        if (hasFocus) {
            setupFullScreen();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (mWebView != null) {
            mWebView.onPause();
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (mWebView != null) {
            mWebView.onResume();
        }
        setupFullScreen();
    }
}
