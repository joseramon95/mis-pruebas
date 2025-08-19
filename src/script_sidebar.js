const sidebar = document.getElementById("sidebar");
const trigger = document.getElementById("trigger");

// Cuando el cursor entra a la franja → muestra el sidebar
trigger.addEventListener("mouseenter", () => {
  sidebar.style.left = "0";
});

// Cuando el cursor sale del sidebar → vuelve a esconderlo
sidebar.addEventListener("mouseleave", () => {
  sidebar.style.left = "-220px";
});
