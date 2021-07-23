def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un número: "))
        if num < 0:
            raise ValueError("Debe ingresar un número positivo.")
        print(divisors(num))
        print("Terminó mi programa.")
    except ValueError as ve:
        if 'invalid literal for int() with base 10:' in str(ve):
            print("Debes ingresar un número")
        else:
            print(ve)
        

if __name__ == '__main__':
    run() 