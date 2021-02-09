import datetime
import http
import json
import pandas as pd
import matplotlib.pyplot as plt


def recommendGolfer():
    # Get data from external API
    json_object = getData()
    # print raw data
    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)
    # select the columns required for the analysis
    df = pd.DataFrame.from_records(json_object['data']
        , columns=['valid_date', 'wind_gust_spd', 'wind_spd', 'precip', 'uv', 'vis'])
    # add a column to derive the recomendation based on the rule set in conditions method
    df['recommended'] = df.apply(conditions, axis=1)
    # plot wind gusts graph
    df.plot(x="valid_date", y=["wind_gust_spd"])
    plt.show()
    # plot wind speed graph
    df.plot(x="valid_date", y=["wind_spd"])
    plt.show()
    # plot uv index graph
    df.plot(x="valid_date", y=["uv"])
    plt.show()
    # plot visibility graph
    df.plot(x="valid_date", y=["vis"])
    plt.show()
    # plot precipitation graph
    df.plot(x="valid_date", y=["precip"])
    plt.show()
    # plot recommendation graph
    plt.plot('valid_date', 'recommended', data=df, linestyle='none', marker='o')
    plt.show()


def getData():
    conn = http.client.HTTPSConnection("weatherbit-v1-mashape.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "aa9ab8c454msh05a5f4ee87de0c3p18d923jsn59ae419e8e70",
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
    }
    conn.request("GET", "/forecast/daily?lat=38.5&lon=-78.5", headers=headers)
    return json.loads(conn.getresponse().read().decode("utf-8"))


def conditions(df):
    if (df['wind_gust_spd'] < 7
            and df['wind_spd'] < 1
            and df['precip'] < 1
            and df['vis'] > 10):
        return 1 # recommended = yes
    else:
        return 0 # recommended = no


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     recommendGolfer()

