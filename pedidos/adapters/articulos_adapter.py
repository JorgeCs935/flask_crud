from pedidos.domain.articulos_port import ArticulosPort
from pedidos.domain.articulo import Articulo
from pedidos import *
from pedidos.helpers.pg_command import PGCommand


class ArticulosAdapter(ArticulosPort):

    def __init__(self, db: PGCommand):
        self.db = db

    def get_by_id(self, id: int) -> Articulo | None:
        fila = self.db.queryone(
            """
            select id, codigo, nombre from articulo where id=%(id)s
            """,
            {"id": id},
        )

        if fila is None:
            return None

        return Articulo(fila["id"], fila["codigo"], fila["nombre"])

    def find_all(self, filtro: str) -> list:
        filas = self.db.queryall(
            """
            select id, codigo, nombre from articulo where nombre LIKE %(filtro)s
            """,
            {"filtro": "%" + filtro + "%"},
        )

        lista = []
        for fila in filas:
            lista.append(Articulo(fila["id"], fila["codigo"], fila["nombre"]))
        return lista

    def save(self, articulo: Articulo) -> None:
        sql = """
        insert into articulo (id, codigo, nombre) 
        values (%(codigo)s, %(codigo)s, %(nombre)s)
        on conflict (id) do update set codigo=%(codigo)s, nombre=%(nombre)s
        """

        self.db.execute(
            sql,
            {"id": articulo.id, "codigo": articulo.codigo, "nombre": articulo.nombre},
        )

    def delete(self, articuloId: int) -> None:
        self.db.execute(
            """
            delete from articulo where id=%(id)s
            """,
            {"id": articuloId},
        )
