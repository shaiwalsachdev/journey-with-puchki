# Journey with Puchki - Mobile & TV App

This directory contains the cross-platform native wrapper and deployment setup for **Journey with Puchki**, running on:
- **Android Phone & Tablet**
- **Android TV & Google TV**
- **Apple iOS (iPhone / iPad)**

The app connects directly to your live production instance:
`https://journey-with-puchki.onrender.com/`

---

## 📱 1. Android Phone & Android TV App

The Android code is located in [`android/`](file:///Users/geekdon/Documents/Journey%20with%20Puchki/mobile_app/android).

### Key Features Included:
- **Unified Single APK:** Works on both touchscreens (phones) and remote-controlled big screens (Android TV).
- **TV D-Pad Navigation:** Highlights buttons and cards with a radiant focus ring when using TV remote arrow keys.
- **Auto-Play Media:** Background audio and video slideshows play automatically without restriction.
- **Screen Wake Lock:** Keeps the TV / Phone screen active during slideshows and memories playback.
- **Hardware Back Button Handling:** Double-tap back prevention so you don't accidentally close the app.
- **Offline / Retry Protection:** Clean connection error handling with retry button if Wi-Fi drops.

### How to Build & Install the APK:
1. Open **Android Studio**.
2. Select **Open Project** and choose [`/Users/geekdon/Documents/Journey with Puchki/mobile_app/android`](file:///Users/geekdon/Documents/Journey%20with%20Puchki/mobile_app/android).
3. Connect your Android phone via USB (or click **Build > Build Bundle(s) / APK(s) > Build APK(s)**).
4. The generated `.apk` will be in:
   `mobile_app/android/app/build/outputs/apk/debug/app-debug.apk`

### Installing on Android TV:
1. Install the free **"Send Files to TV"** app on your TV (from Google Play Store on TV) and on your phone.
2. Send `app-debug.apk` to your TV.
3. Open it on the TV to install! It will appear on your TV home screen with the custom Puchki banner.

---

## 🍏 2. iOS (iPhone / iPad)

Because the site is live on Render with HTTPS:

### Instant Install (Recommended - 10 seconds):
1. Open `https://journey-with-puchki.onrender.com/` in **Safari** on your iPhone.
2. Tap the **Share** button (box with upward arrow).
3. Scroll down and tap **"Add to Home Screen"**.
4. Tap **Add**.
5. It will appear with its custom icon on your iPhone home screen and run standalone in full-screen without Safari browser bars.

---

## 📁 Project Structure

```
mobile_app/
├── android/
│   ├── app/
│   │   ├── src/main/
│   │   │   ├── AndroidManifest.xml       # Phone + TV Leanback manifest
│   │   │   ├── java/com/shaix2/journey/
│   │   │   │   └── MainActivity.java     # Webview, WakeLock & TV remote focus
│   │   │   └── res/
│   │   │       ├── drawable/tv_banner.png # Android TV launcher banner
│   │   │       ├── mipmap-hdpi/          # Phone launcher icon
│   │   │       └── values/               # Strings and Fullscreen theme
│   │   └── build.gradle
│   ├── build.gradle
│   ├── settings.gradle
│   └── gradle/wrapper/
├── ios/                                  # iOS resources
├── manifest.json                         # Web App Manifest for PWA
└── README.md
```
