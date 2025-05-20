document.addEventListener("DOMContentLoaded", function () {
    // Captura o formulário
    const form = document.querySelector("form");

    // Adiciona o evento de submit
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Impede o envio padrão do formulário

        // Captura os valores dos campos
        const nome = document.getElementById("nome").value.trim();
        const email = document.getElementById("email").value.trim();
        const assunto = document.getElementById("assunto").value.trim();
        const mensagem = document.getElementById("mensagem").value.trim();

        // Validação básica
        if (nome === "" || email === "" || assunto === "" || mensagem === "") {
            Swal.fire({
                icon: "warning",
                title: "Campos obrigatórios!",
                text: "Por favor, preencha todos os campos.",
                confirmButtonColor: "#3085d6",
            });
            return;
        }

        // Exibir os dados no console (pode ser enviado para um backend futuramente)
        console.log("Nome:", nome);
        console.log("E-mail:", email);
        console.log("Assunto:", assunto);
        console.log("Mensagem:", mensagem);

        // Exibir mensagem de sucesso para o usuário
        Swal.fire({
            icon: "success",
            title: "Mensagem enviada!",
            text: "Obrigado por entrar em contato. Responderemos em breve!",
            confirmButtonColor: "#3085d6",
        });

        // Limpar o formulário
        form.reset();
    });
});
