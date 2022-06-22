from Mostra_lista import mostra_lista

def ricerca_anagrafica(df_anagrafica):
    lista = [
        "CODOTTICO", "NOME", "IND", "CITTA",
        "PR", "CAP", "TEL", "FAX", "CFISC",
        "PIVA", "SCONTOGEN", "CODPAG", "PAGAMENTO",
        "BANCA", "IBAN", "ABI", "CAB", "AGENZIA",
        "FA", "SPEDI", "PAGCORR", "NOOK", "CODCPA",
        "EMAIL", "PEC", "APPLICATOR",
    ]
    mostra_lista(lista)
    scelta_opzione = int(input("scegliere un numero: "))
    cercare = input("Digitare la ricerca da effettuare: ").upper()
    for numero, nome in enumerate(lista, 1):
        if scelta_opzione == numero:
            if df_anagrafica[nome].dtypes != "object":
                df_tipologia = df_anagrafica[nome].dtypes
                df_anagrafica[nome]= df_anagrafica[nome].astype(str)
                df_filtrato = df_anagrafica[df_anagrafica[nome].str.contains(cercare)]
                #chiedere se serve ritrasformare nel tipo originario
                df_anagrafica[nome]= df_anagrafica[nome].astype(df_tipologia)
                return df_filtrato
            else:
                return (df_anagrafica[df_anagrafica[nome].str.contains(cercare)])