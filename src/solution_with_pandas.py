import pandas as pd
import numpy as np

from src.metadata.ask_sql import AskSql


def read_table_bd(cursor, sql_table):
    cursor.execute(sql_table)
    data = cursor.fetchall()
    columns = [i[0] for i in cursor.description]
    df = pd.DataFrame(data, columns=columns)
    return df


def tiendas_con_compras_de_al_menos_100_clientes_diferentes(cursor):
    """¿Cuáles son las tiendas con compras de al menos 100 clientes diferentes?"""

    sql_tiendas = AskSql.tiendas
    sql_compras = AskSql.compras
    tiendas = read_table_bd(cursor, sql_tiendas)
    compras = read_table_bd(cursor, sql_compras)
    compras_tienda = pd.merge(compras, tiendas, on="id_tienda", how="left")

    clientes_dif = compras_tienda.groupby("tipo_tienda")["id_documento"].nunique()
    clientes_dif = pd.DataFrame(clientes_dif)
    clientes_dif.columns = ["cantidad_clientes"]
    clientes_dif.reset_index(inplace=True)
    return clientes_dif


def barrios_donde_la_mayor_cantidad_de_clientes_unicos_realizan_compras(cursor):
    """¿Cuáles son los 5 barrios donde la mayor cantidad de clientes únicos realizan compras en
     tiendas tipo 'Tienda Regional'?"""

    sql_tiendas = AskSql.tiendas
    sql_compras = AskSql.compras
    sql_barrios = AskSql.barrios
    tiendas = read_table_bd(cursor, sql_tiendas)
    compras = read_table_bd(cursor, sql_compras)
    barrios = read_table_bd(cursor, sql_barrios)

    compras_tienda = pd.merge(compras, tiendas, on="id_tienda", how="left")
    compras_tienda_barrio = pd.merge(
        compras_tienda, barrios, on="id_barrio", how="left"
    )

    cols = ["nombre_barrio", "tipo_tienda"]
    agg = {"id_documento": pd.Series.nunique}
    barrio_tienda = compras_tienda_barrio.groupby(cols).agg(agg)
    barrio_tienda.columns = ["cantidad_clientes"]
    barrio_tienda.reset_index(inplace=True)

    cond = barrio_tienda.tipo_tienda == "Tienda Regional"
    barrios_tienda_regional = barrio_tienda[cond]
    barrios_tienda_regional.sort_values(
        "cantidad_clientes", inplace=True, ascending=False
    )

    barrios_tienda = barrios_tienda_regional.loc[
        :, ["nombre_barrio", "cantidad_clientes"]
    ]

    return barrios_tienda[:5]


def compras_por_encima_percentil_95(cursor):
    """¿Cuáles son las tiendas y sus barrios dónde las compras en el último año estan por enciema
    del percentil 95?"""

    sql_tiendas = AskSql.tiendas
    sql_compras = AskSql.compras
    sql_barrios = AskSql.barrios
    tiendas = read_table_bd(cursor, sql_tiendas)
    compras = read_table_bd(cursor, sql_compras)
    barrios = read_table_bd(cursor, sql_barrios)

    compras_tienda = pd.merge(compras, tiendas, on="id_tienda", how="left")
    compras_tienda_barrio = pd.merge(
        compras_tienda, barrios, on="id_barrio", how="left"
    )
    compras_tienda_barrio['total_compra'] = compras_tienda_barrio['total_compra'].astype(float)

    cols = ['tipo_tienda', 'nombre_barrio']
    agg = {'total_compra': sum}
    max_compras = compras_tienda_barrio.groupby(cols, as_index=False).agg(agg)

    perc_95 = np.percentile(max_compras.total_compra, 95)
    cond = max_compras.total_compra >= perc_95
    max_compras = max_compras[cond]
    max_compras.sort_values('total_compra', ascending=False, inplace=True)
    return max_compras

