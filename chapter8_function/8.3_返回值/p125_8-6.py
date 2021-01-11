def city_country(city, country):
    location = city.title() + ', ' + country.title()
    return location

print(city_country('shanghai', 'beijing'))