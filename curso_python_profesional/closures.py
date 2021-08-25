def repeat_maker(times):
    repeat_n = lambda x: x*times
    return repeat_n

repeat2 = repeat_maker(2)
print(repeat2("facu"))