def factorial(n):
    """
    Calcula el factorial de n.

    n int > 0
    returns n!
    """
    print(n)
    if n == 1:
        return 1
    return n*factorial(n-1)

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    n = int(input("Escribe un entero:"))
    print(f'{n}! es igual a: {factorial(n)}')

