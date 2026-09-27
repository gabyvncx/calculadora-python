while True:
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Divisão inteira')
    print('6 - Módulo / Resto')
    print('7 - Potenciação')
    operação = input('Escolha uma opção:')

    while True:
        try:
            numero1 = float(input('Digite um número:'))
            numero2 = float(input('Digite o segundo número:'))
            break
        except ValueError:
            print('Isso não é um número válido! Tente de novo.')

    if operaçao == '1':
        resultado = numero1 + numero2
        print(resultado)
    elif operaçao == '2':
        resultado = numero1 - numero2
        print(resultado)
    elif operaçao == '3':
        resultado = numero1 * numero2
        print(resultado)
    elif operaçao == '4':
        try:
            resultado = numero1 / numero2
            print(resultado)
        except ZeroDivisionError:
            print('Erro: não é possível dividir por zero!')
    elif operaçao == '5':
        try:
            resultado = numero1 // numero2
            print(resultado)
        except ZeroDivisionError:
            print('Erro: não é possível dividir por zero!')
    elif operaçao == '6':
        try:
            resultado = numero1 % numero2
            print(resultado)
        except ZeroDivisionError:
            print('Erro: não é possível dividir por zero!')
    elif operaçao == '7':
        resultado = numero1 ** numero2
        print(resultado)

    else:
        print('Operação inválida')

    continuar = input('Desejá fazer outro calculo? [S/N]:')
    if continuar != 's':
        break
