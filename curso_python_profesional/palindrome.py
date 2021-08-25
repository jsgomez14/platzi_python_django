def is_palindrome(string :str) -> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]

def is_prime(integer: int) -> bool:
    result = [i for i in range(2,integer) if integer % i == 0]
    return not result 

def run():
    # print(is_palindrome("10001"))
    print(is_prime(720))

if __name__ == "__main__":
    run()