x = [ [5,2,3], [10,8,9] ];
x[1][0] = 15
print(x)

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes['fútbol'][0] = 'andres'
print(directorio_deportes)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

#parte 2

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(estudiantes):
    for e in estudiantes:
        for key,value in e.items():
            print(key, ":", value)

iterateDictionary(estudiantes)

#parte 3

def iterateDictionary2(key_name, some_list):
    for d in some_list:
        print(d[key_name])

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

#parte 4
dojo = {
'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    print(f"{len(dojo['ubicaciones'])} UBICACIONES")
    for ubicacion in dojo['ubicaciones']:
        print(ubicacion)
    print(f"\n{len(dojo['instructores'])} INSTRUCTORES")
    for instructor in dojo['instructores']:
        print(instructor)

printInfo(dojo)


