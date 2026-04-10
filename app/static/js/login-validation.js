document.addEventListener("DOMContentLoaded", function () {
    
    const formNavbar = document.getElementById("formLoginNavbar");
    const erroDivNavbar = document.getElementById("erroLoginNavbar");
    const erroMsgNavbar = document.getElementById("erroMsgNavbar");
    let emailNavbar = document.getElementById("emailNavbar");
    let senhaNavbar = document.getElementById("senhaNavbar");

    if (formNavbar) {
        formNavbar.addEventListener("submit", function (e) {
            // Buscar os elementos novamente para garantir que existem
            emailNavbar = document.getElementById("emailNavbar");
            senhaNavbar = document.getElementById("senhaNavbar");
            
            const email = emailNavbar ? emailNavbar.value.trim() : "";
            const senha = senhaNavbar ? senhaNavbar.value.trim() : "";
            
            console.log("Validando login - Email:", email, "Senha:", senha ? "***" : "vazio");
            
            if (!email || !senha) {
                e.preventDefault();
                if (erroMsgNavbar) erroMsgNavbar.textContent = "Preencha e-mail e senha para entrar.";
                if (erroDivNavbar) erroDivNavbar.classList.remove("d-none");
                return;
            }
            
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                e.preventDefault();
                if (erroMsgNavbar) erroMsgNavbar.textContent = "Digite um e-mail válido (exemplo: usuario@email.com).";
                if (erroDivNavbar) erroDivNavbar.classList.remove("d-none");
                return;
            }
            
            if (erroDivNavbar) erroDivNavbar.classList.add("d-none");
        });
        
        if (emailNavbar) {
            emailNavbar.addEventListener("input", function() {
                if (erroDivNavbar) erroDivNavbar.classList.add("d-none");
            });
        }
        
        if (senhaNavbar) {
            senhaNavbar.addEventListener("input", function() {
                if (erroDivNavbar) erroDivNavbar.classList.add("d-none");
            });
        }
    }

    const formPage = document.getElementById("formLoginPage");
    const erroDivPage = document.getElementById("erroLoginPage");
    const erroMsgPage = document.getElementById("erroMsgPage");
    let emailPage = document.getElementById("emailPage");
    let senhaPage = document.getElementById("senhaPage");

    if (formPage) {
        formPage.addEventListener("submit", function (e) {
            emailPage = document.getElementById("emailPage");
            senhaPage = document.getElementById("senhaPage");
            
            const email = emailPage ? emailPage.value.trim() : "";
            const senha = senhaPage ? senhaPage.value.trim() : "";
            
            // Validar se os campos estão vazios
            if (!email || !senha) {
                e.preventDefault();
                if (erroMsgPage) erroMsgPage.textContent = "Preencha e-mail e senha para entrar.";
                if (erroDivPage) erroDivPage.classList.remove("d-none");
                return;
            }
            
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                e.preventDefault();
                if (erroMsgPage) erroMsgPage.textContent = "Digite um e-mail válido (exemplo: usuario@email.com).";
                if (erroDivPage) erroDivPage.classList.remove("d-none");
                return;
            }
            
            if (erroDivPage) erroDivPage.classList.add("d-none");
        });
        
        if (emailPage) {
            emailPage.addEventListener("input", function() {
                if (erroDivPage) erroDivPage.classList.add("d-none");
            });
        }
        
        if (senhaPage) {
            senhaPage.addEventListener("input", function() {
                if (erroDivPage) erroDivPage.classList.add("d-none");
            });
        }
    }

    const formRegister = document.getElementById("formRegister");
    const erroDivRegister = document.getElementById("erroRegister");
    const erroMsgRegister = document.getElementById("erroMsgRegister");
    let emailRegister = document.getElementById("emailRegister");
    let senhaRegister = document.getElementById("senhaRegister");
    let nomeRegister = document.getElementById("nomeRegister");
    let sobrenomeRegister = document.getElementById("sobrenomeRegister");

    if (formRegister) {
        formRegister.addEventListener("submit", function (e) {
            nomeRegister = document.getElementById("nomeRegister");
            sobrenomeRegister = document.getElementById("sobrenomeRegister");
            emailRegister = document.getElementById("emailRegister");
            senhaRegister = document.getElementById("senhaRegister");
            
            const nome = nomeRegister ? nomeRegister.value.trim() : "";
            const sobrenome = sobrenomeRegister ? sobrenomeRegister.value.trim() : "";
            const email = emailRegister ? emailRegister.value.trim() : "";
            const senha = senhaRegister ? senhaRegister.value.trim() : "";
            
            if (!nome || !sobrenome) {
                e.preventDefault();
                if (erroMsgRegister) erroMsgRegister.textContent = "Preencha seu nome e sobrenome.";
                if (erroDivRegister) erroDivRegister.classList.remove("d-none");
                return;
            }
            
            if (!email || !senha) {
                e.preventDefault();
                if (erroMsgRegister) erroMsgRegister.textContent = "Preencha e-mail e senha para cadastrar.";
                if (erroDivRegister) erroDivRegister.classList.remove("d-none");
                return;
            }
            
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                e.preventDefault();
                if (erroMsgRegister) erroMsgRegister.textContent = "Digite um e-mail válido (exemplo: usuario@email.com).";
                if (erroDivRegister) erroDivRegister.classList.remove("d-none");
                return;
            }
            
            if (senha.length < 3) {
                e.preventDefault();
                if (erroMsgRegister) erroMsgRegister.textContent = "A senha deve ter pelo menos 3 caracteres.";
                if (erroDivRegister) erroDivRegister.classList.remove("d-none");
                return;
            }
            
            if (erroDivRegister) erroDivRegister.classList.add("d-none");
        });
        

        if (emailRegister) {
            emailRegister.addEventListener("input", function() {
                if (erroDivRegister) erroDivRegister.classList.add("d-none");
            });
        }
        
        if (senhaRegister) {
            senhaRegister.addEventListener("input", function() {
                if (erroDivRegister) erroDivRegister.classList.add("d-none");
            });
        }
        
        if (nomeRegister) {
            nomeRegister.addEventListener("input", function() {
                if (erroDivRegister) erroDivRegister.classList.add("d-none");
            });
        }
        
        if (sobrenomeRegister) {
            sobrenomeRegister.addEventListener("input", function() {
                if (erroDivRegister) erroDivRegister.classList.add("d-none");
            });
        }
    }
});