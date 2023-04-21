def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo{nome}")

def exibir_mensagem_3(nome=" Antônio"):
    print(f"Seja bem vindo{nome}")

exibir_mensagem()
exibir_mensagem_2(nome=" Etoo")
exibir_mensagem_3()
exibir_mensagem_3(nome=" Chappie")

def calcular_total(numeros):
    return sum(numeros)

def return_antcessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 34]))
print(return_antcessor_e_sucessor(10))
