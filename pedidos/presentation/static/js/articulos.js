// 1. Mover todas las funciones al ámbito global
window.mostrarModalCrear = function() {
    const modal = new bootstrap.Modal(document.getElementById('crearArticuloModal'));
    modal.show();
};

window.crearArticulo = async function() {
    const codigo = document.getElementById("crearCodigo").value;
    const nombre = document.getElementById("crearNombre").value;
    const precio = document.getElementById("crearPrecio").value;

    try {
        const response = await fetch('/articulos-api', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ codigo, nombre, precio })
        });
        const result = await response.json();
        
        if (result.success === "1") {
            bootstrap.Modal.getInstance(document.getElementById('crearArticuloModal')).hide();
            location.reload();
        } else {
            alert('Error: ' + (result.error || 'Error desconocido'));
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error de conexión');
    }
};

window.cargarArticuloParaEditar = async function(id) {
    try {
        const response = await fetch(`/articulos-api/${id}`);
        const data = await response.json();

        if (data.success === "1") {
            document.getElementById("editId").value = data.articulo.id;
            document.getElementById("editCodigo").value = data.articulo.codigo;
            document.getElementById("editNombre").value = data.articulo.nombre;
            document.getElementById("editPrecio").value = data.articulo.precio;
            
            const modal = new bootstrap.Modal(document.getElementById('editarArticuloModal'));
            modal.show();
        }
    } catch (error) {
        console.error('Error:', error);
    }
};

window.guardarCambios = async function() {
    const id = document.getElementById("editId").value;
    const codigo = document.getElementById("editCodigo").value;
    const nombre = document.getElementById("editNombre").value;
    const precio = document.getElementById("editPrecio").value;

    try {
        const response = await fetch(`/articulos-api/update/${id}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ codigo, nombre, precio })
        });
        const result = await response.json();

        if (result.success === "1") {
            bootstrap.Modal.getInstance(document.getElementById('editarArticuloModal')).hide();
            location.reload();
        }
    } catch (error) {
        console.error('Error:', error);
    }
};

window.prepararEliminar = function(id) {
    window.articuloIdAEliminar = id; // Asegurarse de usar window.
    const modal = new bootstrap.Modal(document.getElementById('modalEliminar'));
    modal.show();
};

// 2. Configurar event listeners cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    // Mover el listener de eliminación aquí
    document.getElementById('confirmarEliminar')?.addEventListener('click', async function() {
        if (!window.articuloIdAEliminar) return;

        try {
            const response = await fetch(`/articulos-api/delete/${window.articuloIdAEliminar}`, {
                method: 'DELETE'
            });
            const result = await response.json();

            if (result.success === "1") {
                bootstrap.Modal.getInstance(document.getElementById('modalEliminar')).hide();
                location.reload();
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });
    
    // 3. Verificar en consola que todo está cargado
    console.log("JavaScript cargado correctamente");
    console.log("Funciones disponibles:", {
        mostrarModalCrear: typeof mostrarModalCrear,
        crearArticulo: typeof crearArticulo,
        cargarArticuloParaEditar: typeof cargarArticuloParaEditar,
        guardarCambios: typeof guardarCambios,
        prepararEliminar: typeof prepararEliminar
    });
});