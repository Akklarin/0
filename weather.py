import requests
#s_city = "Minsk City, BY"
city_id = 625144
appid = "{__MyAPPID__}"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    #d = str(data['weather'][0]['description']) + ", температура " + str(data['main']['temp'])
    d = str((data['weather'][0]['description'], ", температура", data['main']['temp']))
    print(d)
    #print(data['weather'][0]['description'], ", температура", data['main']['temp'])
    #print("temp:", data['main']['temp'])
    # print("temp_min:", data['main']['temp_min'])
    # print("temp_max:", data['main']['temp_max'])
except Exception as e:
    print("Exception (weather):", e)
    pass

