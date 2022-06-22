from Inserimento_anagrafica import inserimento_anagrafica
from Path_anagrafica import df_anagrafica , FILE_PATH
from Ricerca_anagrarica import ricerca_anagrafica
from Modifica_anagrafica import modifica_anagrafica
from Cancellare_anagrafica import cancellare_anagrafica

while True:
    try:
        utente = int(input("1. Mostra anagrafica\n2. Aggiungi ad anagrafica\n3. Cerca da anagrafica\n4. Rimuovi da anagrafica\n5. Modifica Anagrafica\n0. Esci\n"))
        if utente == 0:
            break
        elif utente == 1:
            print(df_anagrafica)
        elif utente == 2:
            inserimento_anagrafica(df_anagrafica, FILE_PATH)
        elif utente == 3:
            print(ricerca_anagrafica(df_anagrafica))
        elif utente == 4:
            cancellare_anagrafica(df_anagrafica,FILE_PATH)
        elif utente == 5:
            modifica_anagrafica(df_anagrafica,FILE_PATH)
        else:
            print("scelta errata")
    except ValueError as err:
        print(f"{err} inserire un numero")        



# 2. alla fine ti chiede se vuoi aggiungere altro di quell'utente
# 3. in caso di risposta affermativa nome cognome si autocompilano --> puoi aggiungere solo piva indiirzzo codcliente