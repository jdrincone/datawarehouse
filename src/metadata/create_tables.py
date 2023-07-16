
class CreateTable:
    """ Creacción de tablas en un motor de Base de datos."""

    documentos = """
    CREATE TABLE IF NOT EXISTS documentos (
                id_documentos                   VARCHAR             NOT NULL      encode  zstd,     
                num_documento_cliente           VARCHAR             NOT NULL      encode  zstd,     
                tipo_documento_cliente          VARCHAR             NULL          encode  bytedict
                );"""

    tiendas = """
    CREATE TABLE IF NOT EXISTS tiendas (
            id_tienda               VARCHAR                  NOT NULL         encode  zstd,     
            codigo_tienda           VARCHAR                  NOT NULL         encode  zstd,  
            tipo_tienda             VARCHAR                  NULL             encode  bytedict,  
            latitud_tienda          DOUBLE PRECISION         NULL             encode  zstd, 
            longitud_tienda         DOUBLE PRECISION         NULL             encode  zstd
            );
    """

    barrios = """
    CREATE TABLE IF NOT EXISTS barrios (
                id_barrio                VARCHAR(50)             NOT NULL      encode  zstd,
                nombre_barrio            VARCHAR(50)             NULL          encode  text255
                );
    """

    compras = """
    CREATE TABLE IF NOT EXISTS compras (
                id_documento                     VARCHAR              NOT NULL      encode  zstd,
                id_tienda                        VARCHAR              NOT NULL      encode  zstd,
                id_barrio                        VARCHAR              NOT NULL      encode  zstd,
                total_compra                     DECIMAL              NOT NULL      encode  zstd,
                fecha_compra                     VARCHAR              NOT NULL      encode  zstd
                );
    """

    tiempos = """
     CREATE TABLE IF NOT EXISTS tiempos (
                fecha_compra                     VARCHAR              NOT NULL      encode  zstd,
                year_compra                      INT                  NOT NULL      encode  bytedict,
                month_compra                     VARCHAR              NOT NULL      encode  bytedict,
                day_compra                       VARCHAR              NOT NULL      encode  bytedict
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
                fecha_compra                             VARCHAR                   NOT NULL,      
                year_compra                              INTEGER                   NOT NULL,     
                month_compra                             VARCHAR                   NOT NULL,     
                day_compra                               VARCHAR                   NOT NULL     
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
                    fecha_compra                             VARCHAR                   NOT NULL,
                    year_compra                              INT                       NOT NULL,    
                    month_compra                             VARCHAR                   NOT NULL,    
                    day_compra                               VARCHAR                   NOT NULL 
                    );"""