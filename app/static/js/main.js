// Auto preenchimento de CEP via ViaCEP (somente na página de cadastro)
document.addEventListener('DOMContentLoaded', function() {
    const campoCep = document.getElementById('cep');
    if (campoCep) {
        campoCep.addEventListener('blur', function() {
            let cep = this.value.replace(/\D/g, '');
            if (cep.length === 8) {
                fetch(`https://viacep.com.br/ws/${cep}/json/`)
                    .then(resposta => resposta.json())
                    .then(dados => {
                        if (!dados.erro) {
                            const rua = document.getElementById('rua');
                            const cidade = document.getElementById('cidade');
                            const estado = document.getElementById('estado');
                            if (rua) rua.value = dados.logradouro || '';
                            if (cidade) cidade.value = dados.localidade || '';
                            if (estado) estado.value = dados.uf || '';
                        } else {
                            console.warn('CEP não encontrado');
                        }
                    })
                    .catch(erro => console.error('Erro ao buscar CEP:', erro));
            }
        });
    }

    // Máscara simples para CEP (opcional)
    if (campoCep) {
        campoCep.addEventListener('input', function(e) {
            let valor = e.target.value.replace(/\D/g, '');
            if (valor.length > 5) {
                valor = valor.substring(0,5) + '-' + valor.substring(5,8);
            }
            e.target.value = valor;
        });
    }

    // Animação suave para links internos
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', function(e) {
            const destino = document.querySelector(this.getAttribute('href'));
            if (destino) {
                e.preventDefault();
                destino.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});