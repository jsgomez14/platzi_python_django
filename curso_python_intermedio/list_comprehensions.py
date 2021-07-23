
def run():
    squares=[i**2 for i in range(1,101)]
    print("Squares nums:",squares)
    not_div_3 = [i for i in squares if i%3!=0]
    print("Squares nums multiple of 3:",not_div_3)
    #Reto:
    reto = [i for i in range(1,99999) if (i%4==0 and i%6==0 and i%9==0)]
    print("Reto:", reto)

if __name__ == '__main__':
    run()