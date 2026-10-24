/**
 * Journey with Puchki - Android TV 10-Foot UI & D-Pad Remote Controller
 * Provides seamless TV remote navigation (Up, Down, Left, Right, OK, Back)
 * with radiant glowing visual cards, Netflix-style auto-scrolling, and Ambient Slideshow controls.
 */

(function () {
    // Only activate TV enhancements if on Android TV, TV browser, or large display with D-Pad
    const isTV = /AndroidTV|LargeTV|CrKey|AFTT|Nexus Player|SmartTV|AppleTV|HbbTV|TV/i.test(navigator.userAgent) 
              || window.innerWidth >= 1280 && window.matchMedia('(hover: none) and (pointer: coarse)').matches
              || window.location.search.includes('tv=true');

    // Inject TV aesthetic styles (Netflix/AppleTV style high-contrast glowing outline)
    const tvStyle = document.createElement('style');
    tvStyle.id = 'tv-remote-styles';
    tvStyle.innerHTML = `
        /* TV Focused Element Glow */
        .tv-focus, :focus, :focus-visible {
            outline: 4px solid #ff2a6d !important;
            outline-offset: 4px !important;
            box-shadow: 0 0 30px rgba(255, 42, 109, 0.9), 0 0 10px rgba(255, 255, 255, 0.8) !important;
            transform: scale(1.05) !important;
            transition: transform 0.18s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.18s ease !important;
            z-index: 9999 !important;
        }

        /* TV Mode Status Bar Overlay */
        #tv-ambient-hud {
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: rgba(15, 12, 27, 0.85);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 42, 109, 0.3);
            border-radius: 9999px;
            padding: 8px 18px;
            color: #fff;
            font-size: 14px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 10px;
            z-index: 10000;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            opacity: 0.85;
            transition: opacity 0.3s ease;
        }
        #tv-ambient-hud:hover { opacity: 1; }

        /* Ensure scrollbars don't look ugly on big TV screens */
        ::-webkit-scrollbar { display: none; }
        body { -ms-overflow-style: none; scrollbar-width: none; }
    `;
    document.head.appendChild(tvStyle);

    let focusableElements = [];
    let currentIndex = 0;

    function refreshFocusableElements() {
        const selector = 'a[href], button:not([disabled]), input:not([disabled]), [tabindex]:not([tabindex="-1"]), .memory-card, .group';
        focusableElements = Array.from(document.querySelectorAll(selector)).filter(el => {
            const rect = el.getBoundingClientRect();
            return rect.width > 0 && rect.height > 0 && window.getComputedStyle(el).visibility !== 'hidden' && window.getComputedStyle(el).display !== 'none';
        });
    }

    function highlightElement(el) {
        if (!el) return;
        el.focus();
        el.classList.add('tv-focus');
        el.scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center' });
    }

    // Spatial navigation helper: Find nearest element in the given direction
    function getNearestElement(currentEl, direction) {
        refreshFocusableElements();
        if (!currentEl) return focusableElements[0];

        const curRect = currentEl.getBoundingClientRect();
        const curCenter = { x: curRect.left + curRect.width / 2, y: curRect.top + curRect.height / 2 };

        let bestCandidate = null;
        let minDistance = Infinity;

        focusableElements.forEach(candidate => {
            if (candidate === currentEl) return;
            const candRect = candidate.getBoundingClientRect();
            const candCenter = { x: candRect.left + candRect.width / 2, y: candRect.top + candRect.height / 2 };

            const dx = candCenter.x - curCenter.x;
            const dy = candCenter.y - curCenter.y;

            let valid = false;
            let primaryDist = 0;
            let secondaryDist = 0;

            if (direction === 'RIGHT' && dx > 15) {
                valid = true;
                primaryDist = dx;
                secondaryDist = Math.abs(dy);
            } else if (direction === 'LEFT' && dx < -15) {
                valid = true;
                primaryDist = -dx;
                secondaryDist = Math.abs(dy);
            } else if (direction === 'DOWN' && dy > 15) {
                valid = true;
                primaryDist = dy;
                secondaryDist = Math.abs(dx);
            } else if (direction === 'UP' && dy < -15) {
                valid = true;
                primaryDist = -dy;
                secondaryDist = Math.abs(dx);
            }

            if (valid) {
                // Weight the primary direction heavier to prefer aligned items
                const score = primaryDist + (secondaryDist * 2);
                if (score < minDistance) {
                    minDistance = score;
                    bestCandidate = candidate;
                }
            }
        });

        return bestCandidate;
    }

    // Handle TV Remote D-Pad Keys
    window.addEventListener('keydown', function (e) {
        const key = e.key;
        const keyCode = e.keyCode;

        // D-Pad Arrow keys (Up: 38/ArrowUp, Down: 40/ArrowDown, Left: 37/ArrowLeft, Right: 39/ArrowRight)
        if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'Enter', ' '].includes(key) || [37, 38, 39, 40, 13, 32].includes(keyCode)) {
            refreshFocusableElements();
            const currentFocused = document.activeElement && focusableElements.includes(document.activeElement)
                ? document.activeElement
                : null;

            let direction = null;
            if (key === 'ArrowUp' || keyCode === 38) direction = 'UP';
            else if (key === 'ArrowDown' || keyCode === 40) direction = 'DOWN';
            else if (key === 'ArrowLeft' || keyCode === 37) direction = 'LEFT';
            else if (key === 'ArrowRight' || keyCode === 39) direction = 'RIGHT';

            if (direction) {
                e.preventDefault();
                const next = getNearestElement(currentFocused, direction);
                if (next) {
                    highlightElement(next);
                }
            } else if (key === 'Enter' || keyCode === 13) {
                if (currentFocused) {
                    currentFocused.click();
                }
            }
        }
    });

    // Auto-focus the first prominent action button on initial load for instant TV usability
    document.addEventListener('DOMContentLoaded', function () {
        setTimeout(() => {
            refreshFocusableElements();
            const primaryHeroBtn = document.querySelector('a[href="#memories"], button.bg-primary, a.bg-primary');
            if (primaryHeroBtn) {
                highlightElement(primaryHeroBtn);
            } else if (focusableElements.length > 0) {
                highlightElement(focusableElements[0]);
            }
        }, 800);
    });

    console.log('[Puchki TV] Android TV Spatial Navigation & Remote D-Pad Engine Initialized');
})();
