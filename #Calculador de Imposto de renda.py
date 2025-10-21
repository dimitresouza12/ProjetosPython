# Calculadora de imposto de renda

#Função para calcular o imposto de renda baseado no salário bruto do cliente
def calcularImposto(salario):
    #Conferir qual a porcentagem e a parcela que será subtraída do valor 
    if salario <= 2428.81:
        imposto = 0
    elif salario > 2428.82 < 2826.65:
        imposto = salario * 0.075 - 182.16
    elif salario > 2826.65 < 3751.06:
        imposto = salario * 0.15 - 394.16
    elif salario > 3751.07 < 4664.68:
        imposto = salario * 0.225 - 675.49
    else:
        imposto = salario * 0.275 - 908.73

    if imposto < 0:
        imposto = 0

    return imposto

# Pergunta qual o salário bruto do cliente
salario_bruto = float(input("Digite seu salário bruto R$:"))

# Calcula o imposto
imposto = calcularImposto(salario_bruto)
# Calcula o salário líquido
salarioLiquido = salario_bruto - imposto 

# Apresenta os resultados
print(f"Salário Bruto é igual a R$: {salario_bruto:.2f}")
print(f"Imposto de renda é igual a R$: {imposto:.2f}")
print(f"Salário líquido é igual a R$: {salarioLiquido:.2f}")
#dsadasadsdadads




                    
