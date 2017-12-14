def build_car(manufacturer, model, **settings):
    car = {"manufacturer": manufacturer, "model": model}
    for key, value in settings.items():
        car[key] = value
    return car


car = build_car("subaru", "outback", color="blue", tow_package=True)
print(car)
