function toggleTheme() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('theme', document.body.classList.contains('dark-mode') ? 'dark' : 'light');
}

// Mantener el tema al recargar
window.onload = () => {
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-mode');
    }
};
<<<<<<< HEAD:static/js/scrips.js


=======
>>>>>>> 049ad2247eab6cf7880927b972c46d30af2df293:proyecto railways/static/js/scrips.js
