class Apartamento:
    def __init__(self, id, numero, torre, vaga=None):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None