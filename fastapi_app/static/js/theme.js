const themes = {
    classic: {
        '--color-primary': '#ec131e',
        '--color-primary-soft': '#fdedee',
        '--color-primary-dark': '#b00e16',
        '--color-primary-light': '#ffebec',
        '--color-bg-light': '#fff0f3',
        '--color-bg-dark': '#221011'
    },
    midnight: {
        '--color-primary': '#6366f1', // Indigo
        '--color-primary-soft': '#e0e7ff',
        '--color-primary-dark': '#4338ca',
        '--color-primary-light': '#c7d2fe',
        '--color-bg-light': '#f8fafc', // Slate 50
        '--color-bg-dark': '#0f172a'   // Slate 900
    },
    roka: {
        '--color-primary': '#d4af37', // Gold
        '--color-primary-soft': '#fffbf0',
        '--color-primary-dark': '#996515',
        '--color-primary-light': '#f9f1d0',
        '--color-bg-light': '#faf9f6', // Off white
        '--color-bg-dark': '#2a1a0f'   // Dark brown
    }
};

function applyTheme(themeName) {
    const theme = themes[themeName] || themes['classic'];
    const root = document.documentElement;

    for (const [property, value] of Object.entries(theme)) {
        root.style.setProperty(property, value);
    }

    // Also save to localStorage for client-side persistence if needed
    localStorage.setItem('theme', themeName);
}

// Function to init theme from server settings or local storage
function initTheme(serverTheme) {
    const savedTheme = localStorage.getItem('theme');
    // Server theme takes precedence if strictly enforcing sync, 
    // but often local override feels faster. 
    // For this app, let's trust the server setting passed down.
    applyTheme(serverTheme || savedTheme || 'classic');
}
