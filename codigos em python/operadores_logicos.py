print(True and True)
print(True and False)
print(True and True)
print(True and False)

saldo = 1000
saque = 200
limite = 100
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)