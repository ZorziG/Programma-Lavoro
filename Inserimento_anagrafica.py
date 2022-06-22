from Conferma_salvataggio import salva
from Mostra_lista import lista
from datetime import date 


def inserimento_anagrafica(df_anagrafica, FILE_PATH):
    inserimento = []
    antecedente = df_anagrafica["CODOTTICO"].iloc[len(df_anagrafica)-1]
    codice = int(antecedente) + 1
    inserimento.append(codice)
    for i in range(1,len(lista())):
        if lista()[i] == "DATAREG":
            data_corrente = date.today()
            inserimento.append(data_corrente)
        else:    
            dato = input(f"Inserisci {lista()[i]}").upper()
            inserimento.append(dato)
    df_anagrafica.loc[len(df_anagrafica)] = inserimento
    salva(df_anagrafica,FILE_PATH)