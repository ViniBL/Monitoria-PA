def soma(m1, m2):
    try:
        return np.add(m1,m2)
    except ValueError:
        print("Tamanhos inconsistentes")
        

