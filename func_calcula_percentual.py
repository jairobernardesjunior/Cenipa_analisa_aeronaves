# cria coluna de percentual da classe sobre o total

def calcula_percentual(df):
    df['perc_ocorr'] = round((df.qtde_ocorr / df.qtde_ocorr.sum()) * 100, 2)

    return df