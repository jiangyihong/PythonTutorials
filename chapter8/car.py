def build_car(manufacturer, model, **settings):
    car = {"manufacturer": manufacturer, "model": model}
    for key, value in settings.items():
        car[key] = value
    return car
