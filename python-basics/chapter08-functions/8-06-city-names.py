def city_country(city, country):
    location = {'city': city.title(), 'country': country.title()}
    return location

location = city_country('spooner', 'united states')
print(location)

location = city_country('dublin', 'ireland')
print(location)

location = city_country('paris', 'france')
print(location)
