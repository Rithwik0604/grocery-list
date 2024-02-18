document.addEventListener("DOMContentLoaded", () => {
    let storageTheme = localStorage.getItem("theme");
    if (storageTheme === null) {
        localStorage.setItem("theme", "dark");
    }
    if (storageTheme === "light") {
        document.body.className = "light";
        document.getElementById("themeIcon").textContent = "light_mode";
    }

})



function toggleTheme() {
    let storageTheme = localStorage.getItem("theme");
    if (storageTheme === "dark") {
        localStorage.setItem("theme", "light")
        document.body.className = "light";
        document.getElementById("themeIcon").textContent = "light_mode";

    }
    else {
        localStorage.setItem("theme", "dark");
        document.body.className = "";
        document.getElementById("themeIcon").textContent = "dark_mode";

    }
}