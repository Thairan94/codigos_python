# saldo = 1500.0
# saque = float(input("Quanto você quer sacar?"))

# if saldo >= saque:
#     print("Aguarde as notas")
# else:
#     print("Saldo insuficiente!")

MAIOR_IDADE = 18

idade = int(input("Informe sua idade:"))

if idade >= 18:
    print("Podes tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Não pdoes tirar a CNH.")
