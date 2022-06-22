from Conferma_salvataggio import salva
from Ricerca_anagrarica import ricerca_anagrafica
import time

def cancellare_anagrafica(df_anagrafica, FILE_PATH):
    df_ricercato = ricerca_anagrafica(df_anagrafica)
    print(df_ricercato)
    i = 0
    print(i)
    while i <= len(df_ricercato.index):
        row = df_ricercato.iloc[i]
        print(row)
        conferma = input("Cancellare l'ottico selezionato? S/N").upper()
        if conferma == "S":
            df_anagrafica = df_anagrafica[df_anagrafica["CODOTTICO"] != row["CODOTTICO"]]
            salva(df_anagrafica,FILE_PATH)
            time.sleep(10)
            break
        else:
            i += 1
          