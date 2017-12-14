responses = {}

while True:
    name = input("What is your name")
    response = input("If you could visit one place in the world, where would you go?")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == "no":
        break
for name, response in responses.items():
    print("%s would like to visit %s " % (name.title(), response))
