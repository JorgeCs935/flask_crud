from flask import render_template, json, request, redirect, url_for, flash
from pedidos.adapters.articulos_adapter import ArticulosAdapter
from pedidos.application.articulo_service import ArticulosService
from pedidos.domain.articulo import Articulo
from pedidos import app
from pedidos import db


@app.route("/articulos", methods=["GET"])
def articulos_index():
    articulos_repository = ArticulosAdapter(db)
    articulosService = ArticulosService(articulos_repository)
    articulos = articulosService.find_all("")
    return render_template("articulos/index.html", articulos=articulos)

@app.route("/articulos/edit/<id>", methods=["GET", "POST"])
def articulos_edit(id):
    articulos_repository = ArticulosAdapter(db)
    articulosService = ArticulosService(articulos_repository)
    articulo = articulosService.get_by_id(id)
    if request.method == "POST":
        articulo.setCodigo(request.form["codigo"])
        articulo.setNombre(request.form["nombre"])
        articulosService.update(articulo)        
        return redirect(url_for("articulos_index"))
    return render_template("articulos/update.html", articulo=articulo)

@app.route("/articulos/create", methods=["GET", "POST"])
def articulos_create():
    if request.method == "POST":
        articulos_repository = ArticulosAdapter(db)
        articulosService = ArticulosService(articulos_repository)
        articuloId = articulosService.get_next_id()
        articulo = Articulo(id=articuloId, codigo=request.form["codigo"], nombre=request.form["nombre"])
        articulosService.add(articulo)
        return redirect(url_for("articulos_index"))
    return render_template("articulos/create.html")


@app.route("/articulos/delete/<id>", methods=["GET", "POST"])
def articulos_delete(id):
    articulos_repository = ArticulosAdapter(db)
    articulosService = ArticulosService(articulos_repository)
    articulo = articulosService.get_by_id(id)
    articulosService.remove(articulo.id())
    flash("Articulo eliminado")
    return redirect(url_for("articulos_index"))