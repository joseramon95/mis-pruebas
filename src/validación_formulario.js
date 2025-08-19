// Validación formulario
document.querySelector('form').addEventListener('submit', function(event) {
    const email = document.getElementById('email').value.trim();
    const nombre = document.getElementById('nombre').value.trim();
    const mensaje = document.getElementById('mensaje').value.trim();

    if (!email || !nombre || !mensaje) {
        alert('Por favor, rellena todos los campos.');
        event.preventDefault();
    }
});