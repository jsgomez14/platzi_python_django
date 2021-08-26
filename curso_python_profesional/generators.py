import time

def fibo_gen(max=None):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        elif max is None or counter <= max:
            aux = n1 + n2
            n1,n2=n2,aux
            counter +=1
            yield aux
        else:
            break

if __name__ == '__main__':
    fibo = fibo_gen(5)
    for i in fibo:
        print(i)
        time.sleep(1)
