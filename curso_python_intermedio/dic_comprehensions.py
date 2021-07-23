def run():
    mega_dic = {k:k**2 for k in range(1,101) if k%3 != 0}
    # print("MegaDic: ", mega_dic)
    #Reto:
    mega_dic = {k:k**(1/2) for k in range(1,1001)}
    print("Reto: ", mega_dic)
if __name__ == '__main__':
    run()