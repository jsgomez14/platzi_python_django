DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] =='python']
    print('all_python_devs',all_python_devs)
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization']=='Platzi']
    print('all_platzi_workers:',all_platzi_workers)
    adults = list(filter(lambda worker: worker['age']>=18,DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    print("adults:",adults)
    old_people = list(map(lambda worker: worker | {"old":worker["age"]>70},DATA))
    print(old_people)
    #RETO:
    all_python_devs = list(filter(lambda w: w['language']=='python',DATA))
    all_python_devs = map(lambda w: w['name'],all_python_devs)
    print('all_python_devs',all_python_devs)
    all_platzi_workers = list(filter(lambda w: w['organization']=='Platzi',DATA))
    all_platzi_workers = map(lambda w: w['name'],all_python_devs)    
    print('all_platzi_workers:',all_platzi_workers)

    adults = [w['name'] for w in DATA if w['age']>=18]
    print("adults:",adults)
    old_people = [w |{"old": w['age']>70} for w in DATA]
    print(old_people)

if __name__ == '__main__':
    run()