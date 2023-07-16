
class InsertTable:
    """Inserta información a tablas existentes en Base de datos."""

    dataset_aux = """INSERT INTO dataset_aux (
            SELECT 
            md5(num_documento_cliente || tipo_documento_cliente) as id_documento,
            md5(codigo_tienda || latitud_tienda || longitud_tienda) as id_tienda,
            *
            FROM dataset
            );"""

    documentos = """INSERT INTO documentos (
            SELECT DISTINCT
                id_documento,
                num_documento_cliente,
                tipo_documento_cliente
            FROM dataset_aux
            );"""

    tiendas = """INSERT INTO tiendas (
            SELECT DISTINCT 
                id_tienda,
                codigo_tienda,
                tipo_tienda,
                latitud_tienda,
                longitud_tienda
            FROM dataset_aux
            );"""

    barrios = """INSERT INTO barrios (
            SELECT 	DISTINCT
                id_barrio,
                nombre_barrio
            FROM dataset_aux
            );"""

    tiempos = """INSERT INTO tiempos (
                SELECT 	DISTINCT
                    fecha_compra,
                    year_compra,
                    month_compra,
                    day_compra
                FROM dataset_aux
                );"""

    compras = """INSERT INTO compras (
            SELECT 	distinct
                id_documento,
                id_tienda,
                id_barrio,
                total_compra,
                fecha_compra
            FROM dataset_aux
            );"""
