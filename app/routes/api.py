from flask import Blueprint, jsonify, request, session
from app.utils.auth import check_basic_auth, log_accion
from app import db
import json

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/socios")
def api_socios():
    from app.models import Socio

    socios = Socio.query.filter_by(activo=True).order_by(Socio.orden).all()
    return jsonify(
        [
            {
                "id": s.id,
                "title": s.nombre,
                "description": s.descripcion,
                "image": s.imagen,
                "contact": {"text": "Contactar", "link": s.whatsapp},
            }
            for s in socios
        ]
    )


@bp.route("/socios/all")
def api_socios_all():
    if "user_id" not in session and not check_basic_auth():
        return jsonify({"error": "No autenticado"}), 401
    from app.models import Socio

    socios = Socio.query.order_by(Socio.orden).all()
    return jsonify(
        [
            {
                "id": s.id,
                "nombre": s.nombre,
                "descripcion": s.descripcion,
                "imagen": s.imagen,
                "whatsapp": s.whatsapp,
                "activo": s.activo,
                "orden": s.orden,
            }
            for s in socios
        ]
    )


@bp.route("/socios", methods=["POST"])
def api_socios_create():
    if "user_id" not in session and not check_basic_auth():
        return jsonify({"error": "No autenticado"}), 401
    from app.models import Socio

    data = request.get_json()
    try:
        orden_value = data.get("orden", 0)
        socio = Socio(
            nombre=data.get("nombre"),
            descripcion=data.get("descripcion", ""),
            imagen=data.get("imagen", ""),
            whatsapp=data.get("whatsapp", ""),
            orden=int(orden_value) if orden_value else 0,
        )
        db.session.add(socio)
        db.session.commit()
        return jsonify({"success": True, "id": socio.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@bp.route("/socios/<int:id>", methods=["PUT"])
def api_socios_update(id):
    if "user_id" not in session and not check_basic_auth():
        return jsonify({"error": "No autenticado"}), 401
    from app.models import Socio

    socio = Socio.query.get_or_404(id)
    data = request.get_json()
    try:
        socio.nombre = data.get("nombre", socio.nombre)
        socio.descripcion = data.get("descripcion", socio.descripcion)
        socio.imagen = data.get("imagen", socio.imagen)
        socio.whatsapp = data.get("whatsapp", socio.whatsapp)
        socio.orden = data.get("orden", socio.orden)
        db.session.commit()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@bp.route("/socios/<int:id>", methods=["DELETE"])
def api_socios_delete(id):
    if "user_id" not in session and not check_basic_auth():
        return jsonify({"error": "No autenticado"}), 401
    from app.models import Socio

    socio = Socio.query.get_or_404(id)
    db.session.delete(socio)
    db.session.commit()
    return jsonify({"success": True})


@bp.route("/socios/<int:id>/toggle", methods=["POST"])
def api_socios_toggle(id):
    if "user_id" not in session and not check_basic_auth():
        return jsonify({"error": "No autenticado"}), 401
    from app.models import Socio

    socio = Socio.query.get_or_404(id)
    socio.activo = not socio.activo
    db.session.commit()
    estado = "activó" if socio.activo else "desactivó"
    log_accion("TOGGLE", "Socios", f"{estado} socio: {socio.nombre}")
    return jsonify({"success": True, "activo": socio.activo})


@bp.route("/componentes")
def api_componentes():
    from app.models import Componente

    componentes = Componente.query.all()
    return jsonify(
        [
            {
                "nombre": c.nombre,
                "titulo": c.titulo,
                "subtitulo": c.subtitulo,
                "contenido": c.contenido,
                "link": c.link,
                "extra_data": c.extra_data,
            }
            for c in componentes
        ]
    )


@bp.route("/componentes/<nombre>")
def api_componente_nombre(nombre):
    from app.models import Componente

    componente = Componente.query.filter_by(nombre=nombre).first()
    if not componente:
        return jsonify({"error": "Componente no encontrado"}), 404
    return jsonify(
        {
            "nombre": componente.nombre,
            "titulo": componente.titulo,
            "subtitulo": componente.subtitulo,
            "contenido": componente.contenido,
            "link": componente.link,
            "extra_data": componente.extra_data,
        }
    )


@bp.route("/contenido/soluciones")
def api_soluciones():
    from app.models import CasoExito

    casos = CasoExito.query.filter_by(activo=True).order_by(CasoExito.orden).all()
    testimonios = []
    for c in casos:
        if c.texto_testimonio:
            testimonios.append(
                {
                    "autor": c.autor_testimonio,
                    "cargo": c.cargo_testimonio,
                    "texto": c.texto_testimonio,
                }
            )
        else:
            testimonios.append(None)

    return jsonify(
        {
            "titulo": "Casos de Éxito",
            "subtitulo": "Descubre cómo hemos ayudado a organizaciones a transformar su incertidumbre en crecimiento.",
            "casos": [
                {
                    "id": c.id,
                    "slug": c.slug,
                    "titulo": c.titulo,
                    "descripcion": c.descripcion,
                    "imagen": c.imagen,
                    "testimonio": testimonios[i],
                }
                for i, c in enumerate(casos)
            ],
        }
    )


@bp.route("/contenido/soluciones/<slug>")
def api_solucion_detalle(slug):
    from app.models import CasoExito

    caso = CasoExito.query.filter_by(slug=slug, activo=True).first()
    if not caso:
        return jsonify({"error": "Caso no encontrado"}), 404

    resultados = []
    if caso.resultados:
        try:
            resultados = json.loads(caso.resultados)
        except:
            resultados = []

    testimonio = None
    if caso.texto_testimonio:
        testimonio = {
            "autor": caso.autor_testimonio,
            "cargo": caso.cargo_testimonio,
            "texto": caso.texto_testimonio,
        }

    return jsonify(
        {
            "id": caso.id,
            "slug": caso.slug,
            "titulo": caso.titulo,
            "descripcion": caso.descripcion,
            "imagen": caso.imagen,
            "contenido": caso.contenido,
            "resultados": resultados,
            "testimonio": testimonio,
        }
    )
