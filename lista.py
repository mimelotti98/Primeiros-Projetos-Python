lista =["jacare","onça","leão","cobra","peixe","galinha"]
lista2 =[1,2,3,4,5]
for i in range(len(lista)):
    print(lista[i])

### Conceitos importantes
lista.append(3) # Adição no final da lista
lista.insert(indice, elemento) #Adição em uma posição especifica
lista.extend(lista2) #Junta duas listas
lista.pop() #Remove o ultimo elemento ou o que você especificar
lista.remove(valor) #Remove um valor especifico da lista, porem remove só o primeiro
lista.count(elemento)#Conta quantas vez o elemento aparece na lista
lista.index(elemento)#Diz qual o indice de um elemente especifico 
lista.sort()#Ordena a lista na ordem crescente
lista.sort(reverse=True)#Ordena a lista em ordem decrescente 
len(lista) #Quantos elementos tem na lista
sum(lista)#Soma todos os elementos da lista
min(lista)#Menor elemento da lista
max(lista)#Maior elemento da lista 
