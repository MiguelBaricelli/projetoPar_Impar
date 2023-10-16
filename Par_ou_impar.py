# Projeto Par ou impar

# Apresentação
print('\n\t\t\t -- Verificador de Número \n\n')

#Entrada

num = int(input('Informe um número'))

# Processamento e saida

if (num % 2) == 0:
    print('\n {} é PAR'.format(num))
else:
    print('\n {} é IMPAR'.format(num))