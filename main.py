from torre import Torre
from apartamento import Apartamento
from fila_espera import FilaEspera
from lista_vagas import ListaVagas


def imprimir_lista(lista):
    atual = lista.inicio
    while atual:
        print(f"Apto {atual.numero} - Vaga {atual.vaga}")
        atual = atual.proximo


def imprimir_fila(fila):
    for ap in fila.fila:
        print(f"Apto {ap.numero}")


# =========================
# INÍCIO DO TESTE
# =========================

print("\n=== Criando torre ===")
torre = Torre(1, "Torre A", "Rua X")

fila = FilaEspera()
lista = ListaVagas()

# Criando apartamentos
a1 = Apartamento(1, "101", torre)
a2 = Apartamento(2, "102", torre)
a3 = Apartamento(3, "103", torre)
a4 = Apartamento(4, "104", torre)

# =========================
# 1. TODOS SEM VAGA - FILA
# =========================
fila.adicionar(a1)
fila.adicionar(a2)
fila.adicionar(a3)
fila.adicionar(a4)

print("\nFila inicial:")
imprimir_fila(fila)

# =========================
# 2. LIBERANDO 2 VAGAS
# =========================
for vaga in [2, 1]:  # propositalmente fora de ordem
    ap = fila.retirar()
    if ap:
        ap.vaga = vaga
        lista.inserir_ordenado(ap)

print("\nLista (deve estar ordenada por vaga):")
imprimir_lista(lista)

print("\nFila após alocar vagas:")
imprimir_fila(fila)

# =========================
# 3. LIBERA UMA VAGA
# =========================
print("\n=== Liberando vaga do apto 101 ===")

removido = lista.remover_por_numero("101")

if removido:
    print(f"Apto {removido.numero} liberou vaga {removido.vaga}")

    proximo = fila.retirar()
    if proximo:
        proximo.vaga = removido.vaga
        lista.inserir_ordenado(proximo)

print("\nLista após redistribuição:")
imprimir_lista(lista)

print("\nFila final:")
imprimir_fila(fila)