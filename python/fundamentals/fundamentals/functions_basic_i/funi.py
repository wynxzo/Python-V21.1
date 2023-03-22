'''
x = [ [5,2,3], [10,8,9] ] 
print(x[0][0])
print(x[0][1])
print(x[0][2])
x[1][0] = 12
x[1][1] = int(x[1][1])
x[1][2]
print(x)

estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(estudiantes[0]['last_name'])
estudiantes[0]['last_name']= 'Bryant'
print(estudiantes)

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes['fútbol'] [0]= "andres"
print(directorio_deportes)

z = [ {'x': 10, 'y': 20} ]
z [0]['y']=30
print(z)
'''
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(estudiantes,name):

    for i in range(len(estudiantes) - len(estudiantes), len(estudiantes)):
        for key, Value in estudiantes[i].items():
            if key == 'last_name':
                print(Value)
        return
    

print(iterateDictionary(estudiantes,'last_name'))



