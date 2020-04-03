def buildCars(country, manufacture, model, **car):
    print(f'My parameters: {car}')

    cars = {country: {}}
    cars[country]['manufacture'] = manufacture
    cars[country]['model'] = model
    for key, value in car.items():
        if type(value) == str:
            print(type(value))
            cars[country][key] = value
        else:
            print(f"Please enter the correct options for your {model}! {value} of {key} isn't correct!")
    return cars


def buildProfile(firstName, lastName, **userProfile):
    profile = {'firstName': firstName, 'lastName': lastName}
    for key, value in userProfile.items():
        profile[key] = value
    return profile
