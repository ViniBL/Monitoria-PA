from sympy.geometry import *
def distancia(obj1, obj2):
    inter = intersection(obj1,obj2)
    
    if(len(inter)) == 1:
        return 0
    if(len(inter)) == 0:
        return None
    else:
        p1,p2 = inter
        return float(p1.distance(p2))

