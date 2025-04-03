package example

import data.cities

default allow = false

allow {
    input.method == "GET"
    input.path == ["api", "public"]
}

allow {
    input.method == "GET"
    input.path == ["api", "data"]
    input.user == "admin"
}
allow {
    print('testing')
    input.method == "GET"
    input.path == ["api", "cities", city_id]
    print(city_id)
    
    # Find matching city
    print(cities)
    some city in cities
    city.id == to_number(city_id)
}
