# from yahoo_weather.weather import YahooWeather
# from yahoo_weather.config.units import Unit
#
#
# data = YahooWeather(APP_ID="K6vcJ8sq",
#                         api_key="dj0yJmk9eWZrS2F2UXNFckNzJmQ9WVdrOVN6WjJZMG80YzNFbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWVk",
#                         api_secret="9b3509311f3e75f55050fb3f3a3a223a4d235e99")
#
#
# def get_weather(city):
#     data.get_yahoo_weather_by_city(city, Unit.celsius)
#     print(data.condition.text)
#     print(data.condition.temperature)
#     for fore in data.forecasts:
#         print(fore.date)
#         print(fore.low)
#         print(fore.high)
import http
import json
import pandas as pd
import requests


def get_weather():
    # conn = http.client.HTTPSConnection("aerisweather1.p.rapidapi.com")
    #
    # headers = {
    #     'x-rapidapi-key': "aa9ab8c454msh05a5f4ee87de0c3p18d923jsn59ae419e8e70",
    #     'x-rapidapi-host': "aerisweather1.p.rapidapi.com"
    # }
    #
    # conn.request("GET", "/forecasts/07307?from=2020-01-01&to=2020-12-31", headers=headers)
    #
    # res = conn.getresponse()
    # data = res.read()
    #
    # json_object = json.loads(data.decode("utf-8"))
    # json_formatted_str = json.dumps(json_object, indent=2)
    # print(json_formatted_str)
    # print(len(json_object))
    # for item in json_object:
    #     print(item.sunrise)
    #     print(item.sunset)

    conn = http.client.HTTPSConnection("weatherbit-v1-mashape.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "aa9ab8c454msh05a5f4ee87de0c3p18d923jsn59ae419e8e70",
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
    }

    conn.request("GET", "/forecast/daily?lat=38.5&lon=-78.5", headers=headers)

    res = conn.getresponse()
    data = res.read()

    json_object = json.loads(data.decode("utf-8"))
    print(len(json_object['data'][0]))
    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)

    # print(pd.DataFrame.from_dict(json_object, orient='columns').T)
    # print(pd.json_normalize(json_object))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     get_weather()

