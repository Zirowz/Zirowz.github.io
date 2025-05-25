document.addEventListener("DOMContentLoaded", () => {
    const registerForm = document.getElementById("registerForm");
    const loginForm = document.getElementById("loginForm");
  
    if (registerForm) {
      registerForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const username = document.getElementById("registerUsername").value;
        const password = document.getElementById("registerPassword").value;
  
        const users = JSON.parse(localStorage.getItem("users")) || {};
  
        if (users[username]) {
          document.getElementById("registerError").textContent = "Ce nom d'utilisateur existe déjà.";
        } else {
          users[username] = password;
          localStorage.setItem("users", JSON.stringify(users));
          alert("Inscription réussie !");
          window.location.href = "index.html";
        }
      });
    }
  
    if (loginForm) {
      loginForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const username = document.getElementById("loginUsername").value;
        const password = document.getElementById("loginPassword").value;
  
        const users = JSON.parse(localStorage.getItem("users")) || {};
  
        if (users[username] && users[username] === password) {
          localStorage.setItem("loggedInUser", username);
          window.location.href = "dashboard.html";
        } else {
          document.getElementById("loginError").textContent = "Identifiants incorrects.";
        }
      });
    }
  });
  