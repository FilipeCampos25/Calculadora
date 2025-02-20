from sympy import symbols, solve, diff, integrate, simplify, sympify, limit
import math

x = symbols("x")

while True:

    print("\ntabela \nraiz: sqrt | potencia: ^ | multiplicação: * | divisão: / \nsin() cos() tan()\n")

    opcao = input("As opções são: /sair/derivar/integrar/calcular/simplificar/limites/: ")

    if opcao == 'sair':
        break

    calculo = input("Digite o cálculo, exemplo: '2 * 3 + x**2': ")

    try:
        expr = sympify(calculo)  # Converte para uma expressão simbólica
    except Exception as e:
        print(f"Erro ao interpretar a expressão: {e}")
        continue

    if opcao == 'calcular':
        resposta = solve(expr)  # Avalia numericamente
    elif opcao == 'simplificar':
        resposta = simplify(expr)
    elif opcao == 'derivar':
        resposta = diff(expr, x)
    elif opcao == 'integrar':
        resposta = integrate(expr, x)
    elif opcao == 'limites':
        tendencia = input("o seu x tende a qual valor x -> ? \n:")
        resposta = limit(expr, x, tendencia)
    else:
        print("Comando inválido, tente novamente.")
        continue

    print(f"\nResultado: {resposta}")
