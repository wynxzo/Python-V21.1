
#cuenta regresiva
def lista(num):
    lista=[]
    for x in range(num,0,-1):
        lista.append(x)
    return lista

print(lista(5) )

#imprimir y devolver
def print_return(list):
    print(list[0])
    return list[1]

print(print_return([1,2]))

#primero más longuitud
def long(list):
    return list[0] + len(list)

print(long([1,2,3,4,5]))

#valores mayores que el segundo
def valores_segundo(list):
    if len(list) < 2:
        return False
    output = []
    for x in range (0,len(list)):
        if list[x] > list[1]:
            output.append(list[x])
    print(len(output))
    return output

print(valores_segundo([5,2,3,2,1,4]))
print(valores_segundo([3]))

#esta longuitud,ese valor
def long_valor(size,valor):
    output = []
    for x in range(0,size):
        output.append(valor)
        return output
    
print(long_valor(4,7))
print(long_valor(6,2))

