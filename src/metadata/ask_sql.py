class AskSql:
    """Preguntas a resolver."""

    """ 1. ¿Cuáles son las tiendas con compras de al menos 100 clientes diferentes? """

    tiendas_comp = """
    SELECT 
        t.tipo_tienda,
        COUNT(DISTINCT id_documento) AS cantidad_clientes
        FROM compras c
        left join tiendas t
        on c.id_tienda=t.id_tienda
        GROUP BY t.tipo_tienda
        HAVING COUNT(DISTINCT id_documento) >= 100;
    """

    """ 2. ¿Cuáles son los 5 barrios donde la mayor cantidad de clientes únicos realizan compras en
     tiendas tipo 'Tienda Regional'?"""

    barrios_tienda = """
    SELECT nombre_barrio,
        COUNT(DISTINCT id_documento) AS cantidad_clientes
        FROM dataset_aux
        WHERE tipo_tienda = 'Tienda Regional'
        GROUP BY nombre_barrio
        ORDER BY cantidad_clientes DESC
        LIMIT 5;
    """

    """3. ¿Cuáles son las tiendas y sus barrios dónde las compras en el último año estan por enciema 
    del percentil 95?"""

    compras_percentil = """
                WITH compras_group AS (
                SELECT 
                    tipo_tienda,
                    nombre_barrio,
                    sum(total_compra) as total
                from dataset
                group by  tipo_tienda, nombre_barrio
                )
            
                    SELECT 
                        tipo_tienda,
                        nombre_barrio,
                        SUM(total) AS total
                    FROM compras_group
                    GROUP BY tipo_tienda, nombre_barrio
                    HAVING SUM(total) > (
                      SELECT PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY total) AS percentile_95
                      FROM compras_group
                    
                    )
                    ORDER BY total DESC"""

    # Extraer tablas completas
    compras = """SELECT * FROM compras"""
    tiendas = """SELECT * FROM tiendas"""
    barrios = """SELECT * FROM barrios"""
