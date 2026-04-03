# Royal Marigold Design System

### 1. Overview & Creative North Star
**Creative North Star: The Modern Heirloom**
Royal Marigold is a design system that bridges the gap between ancient tradition and contemporary digital elegance. It is built to feel like a premium editorial publication—intentional, celebratory, and deeply personal. It eschews the rigid, boxed-in layouts of standard SaaS apps in favor of "The Asymmetric Gallery," where elements overlap, float, and use white space as a narrative tool rather than just a separator.

### 2. Colors
The palette is rooted in the deep rubine of 'Primary' (#c91352), complemented by 'Champagne' and 'Ivory' tones that evoke luxury fabrics and traditional celebratory materials.

*   **The "No-Line" Rule:** Structural borders are strictly prohibited for layout sectioning. Separation must be achieved via background shifts—moving from `surface` to `surface_container_low` (Ivory)—or through the use of the `marigold-pattern` (a subtle 5% opacity radial dot grid).
*   **Surface Hierarchy:** 
    *   `surface`: The default canvas.
    *   `surface_container_low`: Used for large section backgrounds to create a subtle shift in mood.
    *   `surface_container`: Reserved for highlighted cards or "The Royal Gradient" (Ivory to Champagne).
*   **Glass & Gradient:** Floating UI elements (like the navigation bar or location fab) must use an 80% opacity blur (`backdrop-blur-md`) to maintain a sense of lightness and depth.
*   **Signature Textures:** Use the `royal-gradient` (a 135-degree soft gold wash) for elevated content containers.

### 3. Typography
The system uses **Noto Serif** as its primary voice, utilizing its italic variants to create a "Cursive-Title" effect that feels handwritten and bespoke.

*   **Display (3.75rem / 60px):** For hero moments. Bold, tight tracking.
*   **Headline (3rem / 48px):** Used for "Blessings" and major section headers.
*   **Title (1.5rem - 1.875rem):** For milestone names and card titles.
*   **Body (1.125rem / 18px):** High-readability serif for story-telling.
*   **Labels (0.75rem - 0.875rem):** Uses a transition to a cleaner sans-serif or uppercase serif for metadata, such as dates and "Digital Invite" labels.
*   **Signature Scale:** The system utilizes a massive `200px` display font at 10% opacity as a background watermark to break the visual grid.

### 4. Elevation & Depth
Royal Marigold uses "Tonal Layering" and physical-inspired shadows to define hierarchy.

*   **The Layering Principle:** Depth is created by placing `surface` cards over `surface_container_low` backgrounds.
*   **Ambient Shadows:** 
    *   `shadow-sm`: For small interactive components.
    *   `shadow-md`: Standard for milestones.
    *   `shadow-xl`: For parental portraits and "elevated" content.
    *   `shadow-2xl`: Reserved for the Hero Image container and floating action menus.
*   **The Ghost Border:** Where contrast is needed against photography, use an `outline_variant` at 10% opacity or a `4px white/50` solid border to mimic a physical photo frame.

### 5. Components
*   **Buttons:** Must be `rounded-full`. Primary buttons use a solid fill with a high-spread shadow (`shadow-primary/20`). Ghost buttons use uppercase tracking for a luxury feel.
*   **Milestone Cards:** Use a "Greyscale-to-Color" hover transition. Cards should be slightly staggered in the grid (using `translate-y-8`) to avoid a flat, templated look.
*   **The Seal:** A unique component for certifications or highlights (e.g., Kundli Match). Circular, animated (`pulse`), and rotated `12deg` to break the horizontal lines of the screen.
*   **Floral Dividers:** Use Material Symbols (`local_florist`) in a 3-part sequence with thin hairline rules to denote the end of a narrative chapter.

### 6. Do's and Don'ts
*   **Do:** Use italics for quotes and sub-captions to inject personality.
*   **Do:** Allow images to take up significant vertical space (85vh) to establish mood.
*   **Don't:** Use hard black (#000000). Always use the deep plum-tinted `on_surface` (#211116).
*   **Don't:** Align every card perfectly. Use subtle offsets and varying aspect ratios to maintain the "Editorial Gallery" aesthetic.
*   **Do:** Use 10px font sizes sparingly only for "micro-meta" data, ensuring it remains uppercase and tracked out for legibility.