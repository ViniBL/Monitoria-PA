def leia(nome):
    with open(nome) as f:
        lines = f.read()
        return lines
