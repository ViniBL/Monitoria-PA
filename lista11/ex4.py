import datetime
def dia_semana(data):
    dias = ["segunda","terça","quarta","quinta","sexta","sábado","domingo"]
    return dias[data.weekday()]
