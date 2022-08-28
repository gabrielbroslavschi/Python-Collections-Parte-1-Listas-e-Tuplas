idades = [39, 30, 27, 18]
print('teste1')
for idade in idades:
    print(idade)
print()
print()
print()


print('teste2')
print(len(idades))
print(idades)
print()
print()
print()


print('teste3')
idades.append(49)
print(idades)
print()
print()
print()


print('teste4')
print(27 in idades)




print('teste5')
idades.insert(0, 100)
print(idades)
print()
print()
print()



"""print('teste6')
idades.append([27, 19])
print(idades)
for elemento in idades:
    print('Recebi o elemento ', elemento)
print()
print()
print()"""



print('teste7')
idades.extend((18, 19, 20, 21, 32))
for elemento in idades:
    print('Recebi o elemento ', elemento)
print()
print()
print()



print('teste8')
idades_no_ano_que_vem = []
for idade in idades:
    idades_no_ano_que_vem.append(idade + 1)
print('=', idades_no_ano_que_vem)
print()
print()
print()




print('teste9')
print([(idade + 1) for idade in idades])
print()
print()
print()




print('teste10')
print([(idade) for idade in idades if idade > 21])
print()
print()
print()





print('print11')

def faz_processamento_de_visualizacao(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    lista.append(13)

idades = [16, 17, 18, 19, 20, 21]
faz_processamento_de_visualizacao(idades)
print(idades)