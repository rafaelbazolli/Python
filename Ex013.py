salario = float(input('Digite o salário do funcionário: R$ '))
novo = salario + (salario * 0.15)
print('O salário do funcionário era R$ {}.\n'
      'O salário do funcionário após o reajuste é R$ {:.2f}.'.format(salario, novo))
