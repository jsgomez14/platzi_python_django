# [1,1,2,2,4] -> [1,2,4]

def deduplicate(some_list):
    without_duplicates = []
    for e in some_list:
        if e not in without_duplicates:
            without_duplicates.append(e)
    return without_duplicates

def run():
    random_list = [1,1,2,2,4]
    print(deduplicate(random_list))
    print(set(random_list))

if __name__ == '__main__':
    run()