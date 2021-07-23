def run():
    my_list = list(range(10))
    my_dic = {"first_name": "Yanse","last_name":"Gomez"}

    super_list = [
        {"first_name": "Yanse","last_name":"Gomez"},
        {"first_name": "Valen","last_name":"Hernandez"},
        {"first_name": "Ronal","last_name":"Pera"},
        {"first_name": "Francisco","last_name":"Gonzalez"},
        {"first_name": "Pepe","last_name":"Gamez"},
        {"first_name": "Pedro","last_name":"Fernandez"},
    ]

    super_dic = {
        "natural_nums": [1,2,3,4],
        "integer_nums": [-1,-2,0,1,2],
        "float_nums": [1.1,4.5,6.43]
    }

    for key, value in super_dic.items():
        print(key,"-",value)

if __name__ == '__main__':
    run()