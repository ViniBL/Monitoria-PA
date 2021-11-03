import ast
def interpreta(string):
    try:
        return ast.literal_eval(string)
    except Exception as err:
        raise Exception("Tipo Desconhecido")
    
