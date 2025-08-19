
const tooltips = {
    selenium: "Automatización de pruebas web con Python y Selenium, Cuento con años de experiencia y conocimeinto en trabajo real, En situaciones de alto rendimiento",
    pytest: "Pruebas funcionales con PyTest y unittest, con proyectos de retail comercio pequeño",
    sql : "Optimización de consultas SQL y gestión de datos",
    pendiente : "esta nota esta pendinete , luego lo añadire en la siguiente actualizacion",
    unittest : "Experiencia creando pruebas unitarias en Python para validar funciones y garantizar la estabilidad del código, aplicando buenas prácticas de cobertura y organización de test cases.",
    api_testing : "Conocimientos en validación de endpoints REST usando herramientas como Postman y pruebas automatizadas en Python, verificando respuestas, códigos de estado y estructura de datos.",
    ci_cd : "Familiaridad con la integración y entrega continua en entornos de desarrollo, asegurando que las pruebas se ejecuten automáticamente en pipelines para detectar errores tempranamente.",
    Controlversiones : "Uso de Git y GitHub para gestionar proyectos, crear ramas, resolver conflictos y mantener un historial limpio y documentado del código.",
    TestingManual : "Experiencia en ejecución de pruebas funcionales, de regresión y exploratorias, con reporte de incidencias y verificación de criterios de aceptación.",
    documentacion_tecnica :"Elaboración de reportes de pruebas, casos de prueba y guías técnicas, asegurando trazabilidad y claridad para el equipo de desarrollo y QA."
    
};

document.querySelectorAll('.tooltip').forEach(el => {
    const key = el.dataset.tooltip; //.toLowerCase(); // coincide con claves minúsculas
    if (tooltips[key]) {
        const span = document.createElement('span');
        span.className = 'tooltip-text';
        span.textContent = tooltips[key];
        el.appendChild(span);
    }
});
