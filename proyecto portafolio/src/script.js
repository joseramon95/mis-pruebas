// Declarando constantes
const NAVBAR = document.querySelector('.contenedor-header');
const MENU_HAMBURGUESA = document.querySelector('.nav-responsive');
const NAV = document.querySelector('nav'); // Seleccionar el elemento nav

// Agregar evento de scroll para ocultar la barra de navegación y el menú hamburguesa al hacer scroll
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        NAVBAR.classList.add('hidden'); // Ocultar la barra al hacer scroll
        MENU_HAMBURGUESA.classList.add('hidden'); // Ocultar el menú hamburguesa al hacer scroll
    } else {
        NAVBAR.classList.remove('hidden'); // Mostrar la barra al volver arriba
        MENU_HAMBURGUESA.classList.remove('hidden'); // Mostrar el menú hamburguesa al volver arriba
    }
});

// Evento click en el menú hamburguesa para mostrar/ocultar el menú de navegación
MENU_HAMBURGUESA.addEventListener('click', () => {
    NAV.classList.toggle('active'); // Cambiar la clase para mostrar/ocultar el menú
});

// Asegúrate de que el menú se oculte automáticamente si la pantalla es mayor a 768px
window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
        NAV.classList.remove('active'); // Ocultar el menú en pantallas grandes
    }
});

document.querySelector('form').addEventListener('submit', function(event) {
    const email = document.getElementById('email').value;
    const nombre = document.getElementById('nombre').value;
    const mensaje = document.getElementById('mensaje').value;

    if (!email || !nombre || !mensaje) {
        alert('Por favor, rellena todos los campos.');
        event.preventDefault();
    }
});
