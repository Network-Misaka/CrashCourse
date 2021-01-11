magician_names = ['zhang chen', 'zhao yang', 'zhang wei']
temp_list = []


def show_magician(names):
    for name in names:
        print(name)


def make_great(names, changed):
    while names:
        temp = names.pop()
        changed.append(temp)


show_magician(magician_names)
print(magician_names)
# make_great(magician_names[], temp_list) 8-10
make_great(magician_names[:], temp_list)
# 8-11
print(magician_names)
print(temp_list)