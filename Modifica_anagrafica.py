from Ricerca_anagrarica import ricerca_anagrafica
from Mostra_lista import mostra_lista
from Conferma_salvataggio import salva
import time 

def modifica_anagrafica(df_anagrafica,FILE_PATH):
    print("Campo da ricercare")
    df_ricercato = ricerca_anagrafica(df_anagrafica)
    print(df_ricercato)
    i = 0
    print("avvio modifica")
    while i <= len(df_ricercato.index):
        row = df_ricercato.iloc[i]
        print(row)
        conferma = input("Modificare l'ottico selezionato? S/N").upper()
        if conferma == "S":
            lista = [
        "CODOTTICO", "NOME", "IND", "CITTA",
        "PR", "CAP", "TEL", "FAX", "CFISC",
        "PIVA", "SCONTOGEN", "CODPAG", "PAGAMENTO",
        "BANCA", "IBAN", "ABI", "CAB", "AGENZIA",
        "FA", "SPEDI", "PAGCORR", "NOOK", "CODCPA",
        "EMAIL", "PEC", "APPLICATOR",
        ]
            mostra_lista(lista)
            #sistemare il campo da modicare
            nome_colonna= lista[int(input("colonna da modificare"))]
            nuovo_valore = input("inserisci nuovo valore")
            df_anagrafica[nome_colonna].iloc[i] = nuovo_valore
            salva(df_anagrafica,FILE_PATH)
            time.sleep(10)
            break
        else:
            i += 1
