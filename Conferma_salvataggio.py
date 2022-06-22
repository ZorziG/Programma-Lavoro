def salva(df_generico,FILE_PATH_generico):
    try:
        df_generico.to_excel(FILE_PATH_generico, engine="odf", index=False)
    except:
        print("File non salvato")
    else:
        print("File salvato con successo")