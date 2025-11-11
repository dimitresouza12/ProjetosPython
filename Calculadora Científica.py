import math
while True:
    print("---------------------")
    print("|CALCULADORA VIRTUAL|")
    print("---------------------")
    print("[1] Soma")
    print("[2] Subtração")
    print("[3] Multiplicaçaão")
    print("[4] Divisão")
    print("[5] Potenciação")
    print("[6] Radiciação")
    print("[0] Sair")

    opcao = int(input("1- Escolha uma opção: "))
    if(opcao == 1):
        x = int(input("digite o primeiro valor: "))
        y = int(input("digite o segundo valor: "))
        soma = x + y
        print("a soma"," de", x, "+", y, "=", soma)

    elif (opcao == 2):
        x = int(input("digite o primeiro valor: "))
        y = int(input("digite o segundo valor: "))
        subtração = x - y
        print("a subtração", " de", x, "-", y, "=", subtração)

    elif (opcao == 3):
        x = int(input("digite o primeiro valor: "))
        y = int(input("digite o segundo valor: "))
        multiplicação = x * y
        print("a multiplicação", " de", x, "*", y, "=", multiplicação)

    elif (opcao == 4):
        x = int(input("digite o primeiro valor: "))
        y = int(input("digite o segundo valor: "))
        divisão = x * y
        print("a divisão", " de", x, "/", y, "=", divisão)

    elif (opcao == 5):
        x = int(input("digite o valor que deseja calcular: "))
        y = int(input("digite o valor do exponente: "))
        potenciação = x ** y
        print("a potenciação", " de", x, "**", y, "é =", potenciação)

    elif (opcao == 6):
        x = int(input("digite o valor: "))
        radiciação = math.sqrt(x)
        print("a raiz quadrada", "de", x, "é =", radiciação)

    elif opcao == 0:
        print("------------------")
        print("PROGRAMA ENCERRADO")
        print("------------------")

    else:
        print("------------------")
        print("SELECIONE ALGUMA DAS OPÇÕES ACIMA.")
        print("------------------")

    break















