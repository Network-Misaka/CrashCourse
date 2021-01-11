def describe_city(city_name, city_country='china'):
    print(city_name.title() + ' is in ' + city_country.title())

    
describe_city('beijing', 'china')
describe_city('shanghai')
describe_city('new york', 'american')