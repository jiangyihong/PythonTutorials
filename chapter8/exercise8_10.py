def make_great(magician_names):
    i = 0
    while i < len(magician_names):
        magician_names[i] = 'the' + ' ' + magician_names[i]
        i += 1


def show_magicians(magician_names):
    for name in magician_names:
        print(name.title())


magician_names = ['Eisenheim', 'Sophie', 'Inspector Uhl',
                  'Crown Prince Leopold', 'Young Father', 'Josef Fischer']
make_great(magician_names)
show_magicians(magician_names)
