palindromo = lambda texto: texto == texto[::-1]

print(palindromo('ana'))

#High order functions
def saludo(func):
    func()
def hola():
    print("Hola!!")
saludo(hola)
a = [1,4,5,6,9,13,19,21]
b = list(filter( lambda x:x%2!=0,a))
print(b)
a = [1,2,3,4,5]
b = list(map( lambda x:x**2,a))
print(b)

from functools import reduce

a = [2,2,2,2,2]
b = reduce( lambda x,y:x*y,a)
print(b)