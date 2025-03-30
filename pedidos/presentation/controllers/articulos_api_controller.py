from flask import json, request
from pedidos.adapters.articulos_adapter import ArticulosAdapter
from pedidos.application.articulo_service import ArticulosService
from pedidos.domain.articulo import Articulo
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

@app.route("/articulos-api", methods=["POST"])
def articulos_api_create():
    if request.method == "POST":
        articulos_repository = ArticulosAdapter(db)
        articulosService = ArticulosService(articulos_repository)
        
        try:
            articuloId = articulosService.get_next_id()
            data = request.get_json()
            
            articulo = Articulo(
                id=articuloId,
                codigo=data['codigo'],
                nombre=data['nombre']
            )
            
            articulosService.add(articulo)
            
            response_data = {
                "success": "1",
                "message": "Artículo creado exitosamente",
                "id": articuloId
            }
            status_code = 201
        except Exception as e:
            response_data = {
                "success": "0",
                "error": str(e)
            }
            status_code = 400
            
        return app.response_class(
            response=json.dumps(response_data),
            mimetype='application/json',
            status=status_code
        )

@app.route("/articulos-api/update/<id>", methods=["POST", "PUT"])
def articulos_api_update(id):
    articulos_repository = ArticulosAdapter(db)
    articulosService = ArticulosService(articulos_repository)
    articulo = articulosService.get_by_id(id)
    
    if articulo is None:
        data = {
            "success": "0",
            "error": "Articulo no encontrado",
        }
        return app.response_class(
            response=json.dumps(data),
            mimetype='application/json',
            status=404
        )
    
    try:
        data = request.get_json()
        articulo.setCodigo(data['codigo'])
        articulo.setNombre(data['nombre'])
        articulosService.update(articulo)

        response_data = {
            "success": "1",
            "message": "Articulo actualizado"
        }
        status_code = 200
    except Exception as e:
        response_data = {
            "success": "0",
            "error": str(e)
        }
        status_code = 400
    
    return app.response_class(
        response=json.dumps(response_data),
        mimetype='application/json',
        status=status_code
    )

@app.route("/articulos-api/delete/<id>", methods=["DELETE"])
def articulos_api_delete(id):
    articulos_repository = ArticulosAdapter(db)
    articulosService = ArticulosService(articulos_repository)
    
    try:
        articulosService.remove(id)
        response_data = {
            "success": "1",
            "message": "Artículo eliminado"
        }
        status_code = 200
    except Exception as e:
        response_data = {
            "success": "0",
            "error": str(e)
        }
        status_code = 400
    
    return app.response_class(
        response=json.dumps(response_data),
        mimetype='application/json',
        status=status_code
    )