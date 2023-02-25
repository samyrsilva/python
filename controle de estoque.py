print("Controle de Estoque")

# solicita o saldo inicial da peça
saldo = int(input("Digite o saldo inicial da peça: "))
print("Saldo inicial:", saldo)

# executa operações enquanto o usuário quiser continuar
operacao = 0
while operacao != 3:
    print("\nSelecione a operação:")
    print("1 - Compra (entrada) de peças")
    print("2 - Venda (saída) de peças")
    print("3 - Encerrar o programa")
    operacao = int(input("Operação selecionada: "))
    
    if operacao == 1: # compra
        quantidade = int(input("Digite a quantidade de peças compradas: "))
        saldo += quantidade
        print("Saldo atualizado:", saldo)
    elif operacao == 2: # venda
        quantidade = int(input("Digite a quantidade de peças vendidas: "))
        if quantidade <= saldo:
            saldo -= quantidade
            print("Saldo atualizado:", saldo)
        else:
            print("Saldo insuficiente para a venda!")
    elif operacao == 3: # encerrar
        print("Saldo atualizado:", saldo)
        print("Encerrando o programa...")
    else: # operação inválida
        print("Operação inválida!")
