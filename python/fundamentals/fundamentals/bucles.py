lst = list (range(0,151))
print (lst)

lst0 = list (range(0,1001,5))
print(lst0)

for i in range(151):
    print(i)

for i in range(0,1001,5):
    print(i)



for i in range(101):

    if i %5==0:
        print("coding")

    if i %10==0:
        print("Coding Dojo")
    else:
        print(i)


suma=0
for i in range(0,50):
    if i %2 ==0:
        print(i)
        suma = suma +1
        print(suma)           



for i in range(2018, 0, -4):
    print(i)   


lownum= 2
highnum= 9
mult= 3
for i in range(lownum, highnum + 1):
  if i % mult ==0:  
    print(i)     