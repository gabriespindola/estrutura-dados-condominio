class FilaEspera:
    def __init__(self):
        self.fila = []

    def adicionar(self, ap):
        self.fila.append(ap)

    def retirar(self):
        if self.fila:
            return self.fila.pop(0)
        return None