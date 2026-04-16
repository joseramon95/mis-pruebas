from app import create_app

app = create_app()


def init_db():
    from app.models import Usuario, Componente, CasoExito

    with app.app_context():
        db.create_all()

        if not Usuario.query.filter_by(username="root").first():
            root = Usuario(username="root", rol="admin")
            root.set_password("root")
            db.session.add(root)

        componentes_default = [
            {
                "nombre": "Hero",
                "titulo": "Nosotros Resolvemos",
                "subtitulo": "Tus Problemas",
                "contenido": "Soluciones estratégicas de alta complejidad para transformar tu incertidumbre en crecimiento.",
            },
            {
                "nombre": "Features",
                "titulo": "La Arquitectura de la Certeza...",
                "subtitulo": "En un mercado definido...",
                "contenido": "",
            },
            {
                "nombre": "AboutUs",
                "titulo": "Quiénes Somos",
                "subtitulo": "E³: Consultora especializada...",
                "contenido": "",
            },
            {
                "nombre": "MisionVision",
                "titulo": "Misión y Visión",
                "subtitulo": "",
                "contenido": "",
            },
            {
                "nombre": "CTA",
                "titulo": "Listo Para Construir...",
                "subtitulo": "Comienza a construir...",
                "contenido": "",
            },
            {
                "nombre": "Contact",
                "titulo": "Contacto",
                "subtitulo": "¿Tienes preguntas?...",
                "contenido": "",
            },
        ]

        for c in componentes_default:
            if not Componente.query.filter_by(nombre=c["nombre"]).first():
                db.session.add(Componente(**c))

        casos_default = [
            {
                "slug": "transformacion-empresarial",
                "titulo": "Transformación Empresarial",
                "descripcion": "Implementación de estrategia integral de resiliencia organizacional.",
                "imagen": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=600",
                "contenido": "Trabajamos con una empresa del sector manufacturero para transformar su estructura organizacional.",
                "resultados": '["Incremento del 40% en eficiencia operativa", "Reducción del 25% en costos de operación"]',
            },
            {
                "slug": "analisis-de-mercado",
                "titulo": "Análisis de Mercado",
                "descripcion": "Estudio profundo del sector que permitió decisiones estratégicas fundamentadas.",
                "imagen": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600",
                "contenido": "Realizamos un análisis exhaustivo del mercado.",
                "resultados": '["Identificación de 3 nuevos segmentos de mercado", "Incremento del 60% en clientes"]',
            },
            {
                "slug": "planificacion-estrategica",
                "titulo": "Planificación Estratégica",
                "descripcion": "Desarrollo de hoja de ruta para expansión con análisis de riesgo.",
                "imagen": "https://images.unsplash.com/photo-1553877522-43269d4ea984?w=600",
                "contenido": "Desarrollamos un plan estratégico completo.",
                "resultados": '["Plan de expansión a 3 nuevos mercados", "Estructura organizacional para escalar 10x"]',
            },
        ]

        for c in casos_default:
            if not CasoExito.query.filter_by(slug=c["slug"]).first():
                db.session.add(CasoExito(**c))

        db.session.commit()


init_db()  # Descomenta para inicializar DB una vez

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
