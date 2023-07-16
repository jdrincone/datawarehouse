
class CreateTable:
    """ Creacción de tablas en un motor de Base de datos."""

    documentos = """
    CREATE TABLE IF NOT EXISTS documentos (
                id_documentos                   VARCHAR             NOT NULL,
                num_documento_cliente           VARCHAR             NOT NULL,
                tipo_documento_cliente          VARCHAR             NULL
                );"""

    tiendas = """
    CREATE TABLE IF NOT EXISTS tiendas (
            id_tienda               VARCHAR                  NOT NULL          SORTKEY         DISTKEY,
            codigo_tienda           VARCHAR                  NOT NULL,
            tipo_tienda             VARCHAR                  NULL,
            latitud_tienda          DOUBLE PRECISION         NULL,
            longitud_tienda         DOUBLE PRECISION         NULL
            );
    """

    barrios = """
    CREATE TABLE IF NOT EXISTS barrios (
                id_barrio                VARCHAR(50)             NOT NULL            SORTKEY            DISTKEY,
                nombre_barrio            VARCHAR(50)             NULL
                );
    """

    compras = """
    CREATE TABLE IF NOT EXISTS compras (
                id_documento                     VARCHAR              NOT NULL,
                id_tienda                        VARCHAR              NOT NULL,
                id_barrio                        VARCHAR              NOT NULL,
                total_compra                     DECIMAL              NOT NULL,
                fecha_compra                     VARCHAR              NOT NULL
                );
    """

    dataset = """
    CREATE TABLE IF NOT EXISTS dataset (
                num_documento_cliente                    VARCHAR                   NOT NULL,
                tipo_documento_cliente                   VARCHAR                   NOT NULL,
                codigo_tienda                            VARCHAR                   NOT NULL,
                total_compra                             VARCHAR                   NOT NULL,
                tipo_tienda                              VARCHAR                   NOT NULL,
                latitud_tienda                           DOUBLE PRECISION          NOT NULL,
                longitud_tienda                          DOUBLE PRECISION          NOT NULL,
                id_barrio                                VARCHAR                   NOT NULL,
                nombre_barrio                            VARCHAR                   NOT NULL, 
                fecha_compra                             VARCHAR                   NOT NULL
                );"""

    dataset_aux = """
        CREATE TABLE IF NOT EXISTS dataset_aux (
                    id_documento                             VARCHAR                   NOT NULL,
                    id_tienda                                VARCHAR                   NOT NULL,
                    num_documento_cliente                    VARCHAR                   NOT NULL,
                    tipo_documento_cliente                   VARCHAR                   NOT NULL,
                    codigo_tienda                            VARCHAR                   NOT NULL,
                    total_compra                             VARCHAR                   NOT NULL,
                    tipo_tienda                              VARCHAR                   NOT NULL,
                    latitud_tienda                           DOUBLE PRECISION          NOT NULL,
                    longitud_tienda                          DOUBLE PRECISION          NOT NULL,
                    id_barrio                                VARCHAR                   NOT NULL,
                    nombre_barrio                            VARCHAR                   NOT NULL, 
                    fecha_compra                             VARCHAR                   NOT NULL
                    );"""