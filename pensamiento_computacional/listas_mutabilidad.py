a = [1,2,3]
b = a
c = [a,b]
print(a, id(a))
print(b, id(b))
print(c, id(c))
b[0]='a'
print(c, id(c))
print(a, id(a))

#Para clonar a:
a = [1,2,3]
b = list(a)
c = a[::]
print(a, id(a))
print(b, id(b))
print(c, id(c))

#list comprehension:

my_list = list(range(100))
doubled = [i*2 for i in my_list]
print(doubled)
pares = [i for i in my_list if i%2==0]
print(pares)