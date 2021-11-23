import datetime
def dia_semana(data):
    dias = ["segunda","terça","quarta","quinta","sexta","sabado","domingo"]
    return dias[data.weekday()]
