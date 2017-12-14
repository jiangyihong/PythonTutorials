favorite_numbers = {
    'joe':[1,3,45,9],
    'ken':[3,6,7],
    'Peter':[10,56,89]
}
for username,numbers in favorite_numbers.items():
    print('\n %s\' favorite number is: ' % username.title())
    for number in numbers:
        print('\t %d ' % number)