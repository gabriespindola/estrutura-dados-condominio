class ListaVagas:
    def __init__(self):
        self.inicio = None

    def inserir_ordenado(self, ap):
        if self.inicio is None or ap.vaga < self.inicio.vaga:
            ap.proximo = self.inicio
            self.inicio = ap
            return

        atual = self.inicio
        while atual.proximo and atual.proximo.vaga < ap.vaga:
            atual = atual.proximo

        ap.proximo = atual.proximo
        atual.proximo = ap


    def remover_por_numero(self, numero):
        atual = self.inicio
        anterior = None

        while atual:
            if atual.numero == numero:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo
                return atual

            anterior = atual
            atual = atual.proximo

        return None    