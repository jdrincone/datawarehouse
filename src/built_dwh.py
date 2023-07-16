# External libraries
import logging
import pandas as pd

# My libraries
from src.metadata.create_tables import CreateTable as CT
from src.metadata.copytable import CopyTable
from src.metadata.drop_tables import DropTable as DT
from src.metadata.insert_table import InsertTable as Ins


logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def built_dwh(cur, conn, list_table):
    for query in list_table:
        cur.execute(query)
        conn.commit()


def drop_tables(cur, conn):
    """Elimina tablas preexistentes para poder crearlas desde cero."""

    drop_table_queries = [
        DT.dataset,
        DT.dataset_aux,
        DT.barrios,
        DT.compras,
        DT.documentos,
        DT.tiendas,
    ]
    built_dwh(cur, conn, drop_table_queries)
    logger.info("Drop Tables...")


def create_tables(cur, conn):
    """Crea tablas provisionales y dimensionales declaradas en el script sql_queries."""

    create_table_queries = [
        CT.dataset,
        CT.dataset_aux,
        CT.barrios,
        CT.compras,
        CT.documentos,
        CT.tiendas,
    ]
    built_dwh(cur, conn, create_table_queries)
    logger.info("Created Tables...")


def load_staging_tables(cur, conn):
    """Cargue datos de archivos almacenados en S3 en las tablas provisionales mediante las consultas
    declarado en el script sql_queries."""

    copy_table_queries = [CopyTable.dataset]
    built_dwh(cur, conn, copy_table_queries)
    logger.info("Copy principal Table...")


def insert_info_to_table(cur, conn):
    """Inserta información en tablas creadas."""

    insert_table = [
        Ins.dataset_aux,
        Ins.documentos,
        Ins.tiendas,
        Ins.barrios,
        Ins.compras,
    ]
    built_dwh(cur, conn, insert_table)
    logger.info("Insert info in Table...")


def show_ask_sql(ask, cursor, name=""):
    """Muestra en pantalla los resultados de una consulta.

    Args:
        ask: Consulta a resolver en formato sql.
        cursor: cursor inicializado.
        name: Nombre o tipo de pregunta a resolver."""

    cursor.execute(ask)
    data = cursor.fetchall()
    columns = [i[0] for i in cursor.description]
    df = pd.DataFrame(data, columns=columns)
    logger.info(f"{name}")
    logger.info(f".......DataFrame......")
    logger.info(f" {df}")
