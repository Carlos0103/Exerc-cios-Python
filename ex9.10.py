def importar_modulo(nome_modulo):
    try:
        modulo = __import__(nome_modulo)
        print(f"O módulo '{nome_modulo}' foi importado com sucesso.")
    except ModuleNotFoundError:
        print(f"O módulo '{nome_modulo}' não foi encontrado.")
    finally:
        print("Operação finalizada.")


importar_modulo("math")
importar_modulo("módulo_aleatorio")