import pycountry

def countries_list():
    data = []
    for i in pycountry.countries:
        country_data = {"name": i.name, "code": i.numeric}
        data.append(country_data)
    return data