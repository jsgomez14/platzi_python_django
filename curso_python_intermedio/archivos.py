def read():
    numbers = []
    with open("./curso_python_intermedio/archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)

def write():
    names = ["Yanse", "Bolo", "Crack", "Rocío", "Nicolás"]
    with open("./curso_python_intermedio/archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()

if __name__ == '__main__':
    run()