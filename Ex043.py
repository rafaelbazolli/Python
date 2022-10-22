#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso / – Entre 18,5 e 25: Peso Ideal / – 25 até 30: Sobrepeso /
# – 30 até 40: Obesidade / Acima de 40: Obesidade Mórbida
color = {'limpa':'\033[m', 'vermelho':'\033[31m', 'azulclaro':'\033[36m'}
titulo = 'CALCULADORA DE IMC'
print('--='*30, '\n{}{:^90}{}\n'.format(color['azulclaro'], titulo, color['limpa']),'--='*30)
peso = float(input('Digite o peso(Kg): '))
altura = float(input('Digite a altura(m): '))
imc = peso / (altura ** 2)

print('\nO IMC dessa pessoa é: {:.2f}.'.format(imc))
if imc < 18.5:
    print('Você está {}ABAIXO DO PESO{}.'.format(color['vermelho'], color['limpa']))
elif 18.5 <= imc < 25:
    print('Parabéns! Você está na faixa de {}PESO NORMAL{}.'.format(color['azulclaro'], color['limpa']))
elif 25 <= imc < 30:
    print('Você está com {}SOBREPESO{}.'.format(color['vermelho'], color['limpa']))
elif 30 <= imc < 40:
    print('Cuidado! Você está com {}OBESIDADE!{}'.format(color['vermelho'], color['limpa']))
else:
    print('Cuidado! Você está com {}OBESIDADE MÓRBIDA{}!'.format(color['vermelho'], color['limpa']))
