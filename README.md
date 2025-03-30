# INSTALACIÓN
conda create --prefix ./env python
conda activate 
pip install flask
pip install "psycopg[binary,pool]"
conda install flask_cors

# Pasos para crear la base de datos

Crear un servidor en postgres
el usuario debe tener de nombre postgres (cualquier nombre al servidor, contraseña del servidor: 12345) en localhost
Dentro crear una base de datos (Nombre: Almacen)

usando la query tool crear la siguiente tabla(Solo hacer correr el siguiente query)
CREATE SEQUENCE articulo_id_seq START WITH 1 INCREMENT BY 1;

CREATE TABLE articulo (
    id INTEGER PRIMARY KEY DEFAULT nextval('articulo_id_seq'),
    codigo VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    -- Campos adicionales recomendados para un sistema de pedidos:
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE
);


# Ejecución en modo desarrollo
conda activate ./env
flask --app app run
