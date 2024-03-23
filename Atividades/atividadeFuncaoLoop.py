def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 

def menu():
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

def calculadora():
    while True:
        menu()
        opcao = input("Escolha a opção do Menu: ")

        if opcao == '0':
            break
        elif opcao not in ['1', '2', '3', '4']:
            print("Opção Inválida.\n")
            continue

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            resultado = soma(num1, num2)
            print("Resultado: ", resultado)
        elif opcao == '2':
            resultado = subtracao(num1, num2)
            print("Resultado: ", resultado)
        elif opcao == '3':
            resultado = multiplicacao(num1, num2)
            print("Resultado: ", resultado)
        elif opcao == '4':
            resultado = divisao(num1, num2)
            print("Resultado: ", resultado)

        print()  

calculadora()
