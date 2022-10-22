# (1 , 11) , onde o primeiro num é literalmente onde você quer que ele comece a contar,
# e o final precisa ser +1,senão ele acaba no num que estiver após a virgula e o exclui
n = int(input('Digite um número: '))

for c in range(0, n+1):
    print(c)
print('FIM')