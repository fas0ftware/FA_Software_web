// Theme toggle: follows the system preference until the visitor picks a theme,
// then remembers that choice in localStorage.
(function () {
  const THEME_STORAGE_KEY = "theme";
  const rootElement = document.documentElement;
  const toggleButton = document.querySelector(".theme-toggle");
  const toggleLabel = document.querySelector(".theme-toggle__label");
  const systemDarkQuery = window.matchMedia("(prefers-color-scheme: dark)");

  function getStoredTheme() {
    try {
      const storedTheme = localStorage.getItem(THEME_STORAGE_KEY);
      return storedTheme === "light" || storedTheme === "dark" ? storedTheme : null;
    } catch (error) {
      return null;
    }
  }

  function storeTheme(theme) {
    try {
      localStorage.setItem(THEME_STORAGE_KEY, theme);
    } catch (error) {
      // Storage unavailable (e.g. private mode): the theme still applies for this visit.
    }
  }

  function applyTheme(theme) {
    rootElement.dataset.theme = theme;
    const nextTheme = theme === "dark" ? "light" : "dark";
    toggleLabel.textContent = nextTheme === "dark" ? "Dark" : "Light";
    toggleButton.setAttribute("aria-label", "Switch to " + nextTheme + " mode");
  }

  applyTheme(getStoredTheme() || (systemDarkQuery.matches ? "dark" : "light"));

  toggleButton.addEventListener("click", function () {
    const newTheme = rootElement.dataset.theme === "dark" ? "light" : "dark";
    applyTheme(newTheme);
    storeTheme(newTheme);
  });

  // Keep following the system setting while the visitor hasn't chosen a theme.
  systemDarkQuery.addEventListener("change", function (event) {
    if (!getStoredTheme()) {
      applyTheme(event.matches ? "dark" : "light");
    }
  });
})();

// Lightbox: a screenshot button opens its full image in a <dialog>.
(function () {
  const dialog = document.querySelector(".lightbox");
  if (!dialog || typeof dialog.showModal !== "function") return;
  const image = dialog.querySelector(".lightbox__img");

  document.querySelectorAll(".shot").forEach(function (button) {
    button.addEventListener("click", function () {
      const thumb = button.querySelector("img");
      image.src = button.dataset.full;
      image.alt = thumb ? thumb.alt : "";
      dialog.showModal();
    });
  });

  dialog.querySelector(".lightbox__close").addEventListener("click", function () {
    dialog.close();
  });

  // A click on the dark backdrop (outside the image) closes it too.
  dialog.addEventListener("click", function (event) {
    if (event.target === dialog) dialog.close();
  });
})();
