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
                            const bairro = document.getElementById('bairro');
                            const cidade = document.getElementById('cidade');
                            const estado = document.getElementById('estado');

                            if (rua) rua.value = dados.logradouro || '';
                            if (bairro) bairro.value = dados.bairro || '';
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

    if (campoCep) {
        campoCep.addEventListener('input', function(e) {
            let valor = e.target.value.replace(/\D/g, '');
            if (valor.length > 5) {
                valor = valor.substring(0,5) + '-' + valor.substring(5,8);
            }
            e.target.value = valor;
        });
    }

    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', function(e) {
            const destino = document.querySelector(this.getAttribute('href'));
            if (destino) {
                e.preventDefault();
                destino.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const mainConteudo = document.querySelector('.main-conteudo');

    if (navbarToggler && navbarCollapse && mainConteudo) {
        function ajustarMargemConteudo() {
            if (window.innerWidth < 992) {
                if (navbarCollapse.classList.contains('show')) {
                    const alturaMenu = navbarCollapse.scrollHeight;
                    mainConteudo.style.marginTop = (75 + alturaMenu) + 'px';
                } else {
                    mainConteudo.style.marginTop = '75px';
                }
            } else {
                mainConteudo.style.marginTop = '90px';
            }
        }

        navbarToggler.addEventListener('click', function() {
            setTimeout(ajustarMargemConteudo, 300);
        });

        navbarCollapse.addEventListener('hidden.bs.collapse', function() {
            mainConteudo.style.marginTop = '75px';
        });

        navbarCollapse.addEventListener('shown.bs.collapse', function() {
            ajustarMargemConteudo();
        });

        window.addEventListener('resize', function() {
            if (window.innerWidth >= 992) {
                mainConteudo.style.marginTop = '90px';
            } else {
                if (!navbarCollapse.classList.contains('show')) {
                    mainConteudo.style.marginTop = '75px';
                }
            }
        });
    }
});

const checkboxSN = document.getElementById("semNumero");
const campoNumero = document.getElementById("numero");

if (checkboxSN && campoNumero) {
    checkboxSN.addEventListener("change", function () {
        if (this.checked) {
            campoNumero.value = "S/N";
            campoNumero.disabled = true;
        } else {
            campoNumero.value = "";
            campoNumero.disabled = false;
        }
    });
}

document.addEventListener("DOMContentLoaded", function () {
    const campoCep = document.querySelector('input[name="cep"]');

    if (campoCep) {
        campoCep.addEventListener("input", function (e) {
            let valor = e.target.value.replace(/\D/g, "");

            if (valor.length > 5) {
                valor = valor.substring(0, 5) + "-" + valor.substring(5, 8);
            }

            e.target.value = valor;
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const cepInput = document.getElementById("cepInput");

    if (cepInput) {
        const form = cepInput.closest("form");

        form.addEventListener("submit", function (e) {
            const cep = cepInput.value.replace(/\D/g, "");

            if (cep && cep.length < 8) {
                e.preventDefault();
                alert("Digite um CEP completo.");
            }
        });
    }
});