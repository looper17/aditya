// Theme toggle with localStorage persistence
(function() {
  const STORAGE_KEY = 'theme-preference';

  // Get theme preference from localStorage or system preference
  function getThemePreference() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
      return stored;
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  // Set theme
  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(STORAGE_KEY, theme);
  }

  // Initialize theme on page load
  const currentTheme = getThemePreference();
  setTheme(currentTheme);

  // Toggle theme on button click
  document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('theme-toggle');

    if (toggleButton) {
      toggleButton.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
      });
    }
  });
})();
