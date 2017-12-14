def make_great(magician_names, great_magician_names):
    while magician_names:
        current_magician_name = magician_names.pop()
        current_magician_name = "the" + " " + current_magician_name
        great_magician_names.append(current_magician_name)


def show_magicians(magician_names):
    for name in magician_names:
        print(name.title())


magician_names = ['Eisenheim', 'Sophie', 'Inspector Uhl',
                  'Crown Prince Leopold', 'Young Father', 'Josef Fischer']
great_magician_names = []
make_great(magician_names[:], great_magician_names)
show_magicians(great_magician_names)
