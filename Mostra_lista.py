def lista():
    lista = [
        "CODOTTICO", "NOME", "IND", "CITTA", "PR", "CAP",
        "NOME2", "IND2", "CITTA2", "PR2", "CAP2", "TEL", "FAX",
        "CFISC", "PIVA", "SCONTOGEN", "CODPAG", "PAGAMENTO",
        "BANCA", "IBAN", "ABI", "CAB", "FA", "SPEDI", "PAGCORR",
        "NOTE", "DATAREG", "CODCPA", "EMAIL", "PEC", "APPLICATOR",
    ]
    return lista

def mostra_lista():
    
    for numero, nome in enumerate(lista(), 1):
        print(f"{numero}. {nome}")


#qua ha senso fare una classe se voglio mettere un altra lista piu corta?