const fondos = [
  "https://media.giphy.com/media/SS8CV2rQdlYNLtBCiF/giphy.gif",
  "https://media.giphy.com/media/kH6CqYiquZawmU1HI6/giphy.gif",
  "https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif",
  "https://media.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif"
];

let index = 0;

function cambiarFondo() {
  document.body.style.background = `url(${fondos[index]}) center center / cover no-repeat fixed`;
  index = (index + 1) % fondos.length;
}

// Fondo inicial
cambiarFondo();

// Cambia cada 2 segundos
setInterval(cambiarFondo, 2000);
