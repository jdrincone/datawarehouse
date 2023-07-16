
class DropTable:
    """Elimina tablas existentes en Base de datos."""

    documentos = "DROP TABLE IF EXISTS documentos;"
    tiendas = "DROP TABLE IF EXISTS tiendas;"
    barrios = "DROP TABLE IF EXISTS barrios"
    compras = "DROP TABLE IF EXISTS compras;"
    dataset = "DROP TABLE IF EXISTS dataset;"
    dataset_aux = "DROP TABLE IF EXISTS dataset_aux;"
