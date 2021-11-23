import datetime
def existe(dia, mes, ano):
    try:
        x = datetime.datetime(ano, mes, dia)
        return True
    except:
        return False
    