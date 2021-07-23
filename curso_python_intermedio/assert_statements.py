def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Ingresa un número: ")
    assert num.strip('-').isnumeric(), "Debes ingresar un numero"
    num = int(num)
    assert num > 0, "Debes ingresar un numero positivo"
    print(divisors(num))
    print("Terminó mi programa.")
        

if __name__ == '__main__':
    run() 