# separa colunas de classe com hora, elimina nulos e cria período
def separa_elimina_cria(df_acidentes_aux):
    import pandas as pd
    from func_monta_periodo import monta_periodo

    #df_acidentes_aux = df_acidentes_aux.dropna()
    df_acidentes_aux['ocorrencia_hora'] = pd.to_datetime(df_acidentes_aux.ocorrencia_hora)
    df_acidentes_aux['periodo'] = df_acidentes_aux['ocorrencia_hora'].apply(monta_periodo) 

    return df_acidentes_aux  