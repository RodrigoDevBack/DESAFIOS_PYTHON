valor_em_lista = []

def pegar_valor():
    while(True):
        valor_em_lista = []
        valor_a_averiguar = input("Digite algum número: ")
        if not (valor_a_averiguar.isdigit()):
            print("Erro!! Digite algum número inteiro e positivo.")
            continue
        valor_em_lista = [int(d) for d in valor_a_averiguar] # List Comprehension [EXPRESSÃO for ITEM in ITERÁVEL if* CONDIÇÃO*] *Pode ser anulado em caso de tudo do ITERÁVEL ser válido.
        return valor_em_lista

valor_em_lista = pegar_valor()

if valor_em_lista == valor_em_lista[::-1]:
    print(f"É um palíndromo.")
else:
    print(f"Isso não é um palíndromo.")
    