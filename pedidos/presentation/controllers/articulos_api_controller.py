from flask import  json, request
from pedidos.adapters.articulos_adapter import ArticulosAdapter
from pedidos.application.articulo_service import ArticulosService
from pedidos import app
from pedidos import db


@app.route("/articulos-api", methods=["GET"])
def articulos_api_get_all():
    articulos_repository = ArticulosAdapter(db)
    articulosService = ArticulosService(articulos_repository)
    articulos = articulosService.find_all("")

    data = []
    for articulo in articulos:
        data.append({
            "id": articulo.id(),
            "codigo": articulo.codigo(),
            "nombre": articulo.nombre()
        })

    return app.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )

@app.route("/articulos-api/<id>", methods=["GET"])
def articulos_api_get_one(id):
    articulos_repository = ArticulosAdapter(db)
    articulosService = ArticulosService(articulos_repository)
    articulo = articulosService.get_by_id(id)

    if(articulo is None):
        data = {
            "success": "0",
            "error": "Articulo no encontrado",
        }
        return app.response_class(
            response=json.dumps(data),
            mimetype='application/json'
        )        

    data = {
        "success": "1",
        "articulo": {
            "id": articulo.id(),
            "codigo": articulo.codigo(),
            "nombre": articulo.nombre()
        }
    }
    return app.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )

@app.route("/articulos-api/update/<id>", methods=["POST"])
def articulos_api_update(id):
    articulos_repository = ArticulosAdapter(db)
    articulosService = ArticulosService(articulos_repository)
    articulo = articulosService.get_by_id(id)
    if request.method == "POST":
        articulo.setCodigo(request.form["codigo"])
        articulo.setNombre(request.form["nombre"])
        articulosService.update(articulo)

        data = {
            "success": "1",
            "message": "Articulo actualizado"
        }
        return app.response_class(
            response=json.dumps(data),
            mimetype='application/json'
        )

