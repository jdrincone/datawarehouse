# External libraries
import logging
import redshift_connector
import yaml


# My libraries
from src.built_dwh import (
    create_tables,
    drop_tables,
    insert_info_to_table,
    load_staging_tables,
    show_ask_sql,
)

from src.metadata.ask_sql import AskSql
from src.metadata.paths import Paths

from src.solution_with_pandas import (
    barrios_donde_la_mayor_cantidad_de_clientes_unicos_realizan_compras,
    compras_por_encima_percentil_95,
    tiendas_con_compras_de_al_menos_100_clientes_diferentes,
)

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


with open(Paths.cred) as file:
    cred = yaml.full_load(file)
cred_redshift = cred["redshift"]
conn = redshift_connector.connect(**cred_redshift)
cursor = conn.cursor()


def main():
    logger.info("Build Watawearehouse...")
    drop_tables(cursor, conn)
    create_tables(cursor, conn)
    load_staging_tables(cursor, conn)
    insert_info_to_table(cursor, conn)
    logger.info("Fin buid Datawarehouse...")
    logger.info(".............")

    # Preguntas
    logger.warning("Solution of questions by sql...")
    # 1.
    logger.info(
        "1. ¿Cuáles son las tiendas con compras de al menos 100 clientes diferentes?"
    )
    df = show_ask_sql(AskSql.tiendas_comp, cursor)
    logger.info(f"Solution: {df}")

    # 2.
    logger.info(
        """2. ¿Cuáles son los 5 barrios donde la mayor cantidad de clientes
                    únicos realizan compras en tiendas tipo 'Tienda Regional'?"""
    )
    df = show_ask_sql(AskSql.barrios_tienda, cursor)
    logger.info(f"Solution: {df}")

    # 3.
    logger.info(
        """¿Cuáles son las tiendas y sus barrios dónde las compras en el último 
                   año estan por encima  del percentil 95?"""
    )
    df = show_ask_sql(AskSql.compras_percentil, cursor)
    logger.info(f"Solution: {df}")
    logger.info(".............")

    logger.warning("Solution of questions by pandas...")
    logger.info(
        "1. ¿Cuáles son las tiendas con compras de al menos 100 clientes diferentes?"
    )
    df = barrios_donde_la_mayor_cantidad_de_clientes_unicos_realizan_compras(cursor)
    logger.info(f"Solution: {df}")

    logger.info(
        """2. ¿Cuáles son los 5 barrios donde la mayor cantidad de clientes 
                      únicos realizan compras en tiendas tipo 'Tienda Regional'?"""
    )
    df = tiendas_con_compras_de_al_menos_100_clientes_diferentes(cursor)
    logger.info(f"Solution: {df}")

    logger.info(
        """¿Cuáles son las tiendas y sus barrios dónde las compras en el último \n
                        año estan por encima  del percentil 95?"""
    )
    df = compras_por_encima_percentil_95(cursor)
    logger.info(f"Solution: {df}")
    logger.info(".............")


if __name__ == "__main__":
    main()
