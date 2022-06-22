from numpy import dtype
import pandas as pd
# import numpy as np
# from Conferma_salvataggio  import salva

FILE_PATH = f".\Anagrafica Ottici.ods"
df_anagrafica = pd.read_excel(FILE_PATH, engine="odf")
# print(df_anagrafica.dtypes)
# df_anagrafica = df_anagrafica.drop('AGENZIA', 1)

# df_anagrafica['DATAREG']=pd.to_datetime(df_anagrafica['DATAREG'])
# print(df_anagrafica.dtypes)
# inseriesce tutti i campi vuoti con fillna e fa diventare la colonna di quel tipo
# df_anagrafica['PIVA']=df_anagrafica['PIVA'].fillna(0).astype(str)

# inseriesce tutti i campi vuoti
# df_anagrafica = df_anagrafica.replace(np.nan,'.',regex=True)
# salva(df_anagrafica,FILE_PATH)



# HO SCOPERTO PERCHè MI DA FLOAT PERCHè MANCANO DEI VALORE E NON PUò METTERE INT, VOLEVO SAPERE SE CAMBIA QUALCOSA Nullable Integer Data Type.
# POTREBBE ESSERE UNA SOLUZIONE

