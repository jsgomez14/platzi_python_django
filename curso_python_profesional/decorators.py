from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'The functions spent {time_elapsed.total_seconds()} seconds')
    return wrapper

@execution_time
def random_func():
    for _ in range(1,100000000):
        pass

print(random_func())