from flask import render_template, session, request, redirect, url_for
from pedidos.application.articulo_service import ArticulosService
from pedidos import app
from pedidos import articulos_repository


@app.route("/articulos")
def articulos_index():
    articulosService = ArticulosService(articulos_repository)
    articulos = articulosService.find_all("")

    return render_template("articulos/index.html", articulos=articulos)


@app.route("/articulos/edit/<id>", methods=["GET", "POST"])
def articulos_edit(id):
    articulosService = ArticulosService(articulos_repository)
    articulos = articulosService.find_all("")

    return render_template("articulos/index.html", articulos=articulos)


@app.route("/articulos/delete/<id>", methods=["GET", "POST"])
def articulos_delete(id):
    articulosService = ArticulosService(articulos_repository)
    articulos = articulosService.find_all("")

    return render_template("articulos/index.html", articulos=articulos)
