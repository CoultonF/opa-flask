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
    input.method == "GET"
    input.path == ["api", "cities", city_id]
    cities[_].id == to_number(city_id)
}

allow {
    input.method == "GET"
    input.path == ["api", "cities", city_id]
    cities[_].id == to_number(input.city_id)
}

# Print all city names for debugging
city_names[name] {
    name == cities[_].name
}