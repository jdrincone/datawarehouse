# External libraries
import redshift_connector
import yaml

# My libraries
from src.metadata.paths import Paths
from src.metadata.ask_sql import AskSql
from src.built_dwh import (
    create_tables,
    insert_info_to_table,
    load_staging_tables,
    drop_tables,
    show_ask_sql,
)
from src.solution_with_pandas import (
    tiendas_con_compras_de_al_menos_100_clientes_diferentes,
    barrios_donde_la_mayor_cantidad_de_clientes_unicos_realizan_compras,
)

with open(Paths.cred) as file:
    cred = yaml.full_load(file)
cred_redshift = cred["redshift"]
conn = redshift_connector.connect(**cred_redshift)
cursor = conn.cursor()


def main():
    drop_tables(cursor, conn)
    create_tables(cursor, conn)
    load_staging_tables(cursor, conn)
    insert_info_to_table(cursor, conn)

    ask_title = (
        "¿Cuáles son las tiendas con compras de al menos 100 clientes diferentes?"
    )
    show_ask_sql(AskSql.tiendas_comp, cursor, ask_title)

    ask_title = """¿Cuáles son los 5 barrios donde la mayor cantidad de clientes \n
                    únicos realizan compras en tiendas tipo 'Tienda Regional'?"""
    show_ask_sql(AskSql.barrios_tienda, cursor, ask_title)

    barrios_donde_la_mayor_cantidad_de_clientes_unicos_realizan_compras(cursor)
    tiendas_con_compras_de_al_menos_100_clientes_diferentes(cursor)


if __name__ == "__main__":
    main()
