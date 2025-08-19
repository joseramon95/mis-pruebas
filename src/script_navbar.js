// Declarando constantes
const NAVBAR = document.querySelector('.contenedor-header');
const NAV = document.querySelector('nav');

// Ocultar navbar y menú hamburguesa al hacer scroll
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        NAVBAR.classList.add('hidden');
    } else {
        NAVBAR.classList.remove('hidden');
    }
});

// Evitar que al hacer clic dentro del menú no se oculte inmediatamente
NAV.addEventListener('click', (e) => {
    e.stopPropagation();
});

// En desktop: ocultar menú si el cursor sale del nav
NAV.addEventListener('mouseleave', () => {
    if (window.innerWidth > 768) {
        NAV.classList.remove('active');
    }
});
