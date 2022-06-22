from Conferma_salvataggio import salva

def inserimento_anagrafica(df_anagrafica, FILE_PATH):
    inserimento = []
    lista = [
        "CODOTTICO", "NOME", "IND", "CITTA", "PR", "CAP",
        "NOME2", "IND2", "CITTA2", "PR2", "CAP2", "TEL", "FAX",
        "CFISC", "PIVA", "SCONTOGEN", "CODPAG", "PAGAMENTO",
        "BANCA", "IBAN", "ABI", "CAB", "FA", "SPEDI", "PAGCORR",
        "NOTE", "DATAREG", "CODCPA", "EMAIL", "PEC", "APPLICATOR",
    ]
    antecedente = df_anagrafica["CODOTTICO"].iloc[len(df_anagrafica)-1]
    codice = int(antecedente) + 1
    inserimento.append(codice)
    for i in range(1,len(lista)):
        dato = input(f"Inserisci {lista[i]}").upper()
        inserimento.append(dato)
    df_anagrafica.loc[len(df_anagrafica)] = inserimento
    salva(df_anagrafica,FILE_PATH)