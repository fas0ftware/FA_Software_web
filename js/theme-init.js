// Apply the saved or system theme before first paint (loaded without defer to avoid a flash).
(function () {
  var root = document.documentElement;
  root.classList.remove("no-js");
  var storedTheme = null;
  try { storedTheme = localStorage.getItem("theme"); } catch (error) {}
  var prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  root.dataset.theme = storedTheme === "light" || storedTheme === "dark" ? storedTheme : (prefersDark ? "dark" : "light");
})();
