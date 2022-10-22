#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual o salário do funcionário? R$ '))

if salario <= 1250:
    novo = salario + (salario*0.15)
else:
    novo = salario + (salario*0.10)

print('O salário anterior era R$ {:.2f}.\nO salário atual é R$ {:.2f}.'.format(salario, novo))
