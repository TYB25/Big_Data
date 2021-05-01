import requests
import simplejson as json
import matplotlib.pyplot as plt
from pyzipcode import ZipCodeDatabase

zip_data = ZipCodeDatabase()
api_key = "66e745173dcc011dba111294749f8fe0"
temp_data = []
hum_graph = []
temp_graph = []
days_graph = list(range(1, 367))

user_input = input("Enter your Zip code to see the average temperature and humidity: ")
zip_input = zip_data[user_input]
lat = zip_input.longitude
lon = zip_input.latitude
weather_data = "https://history.openweathermap.org/data/2.5/aggregated/year?lat={0}&lon={1}&appid={2}".format(lat, lon,
                                                                                                              api_key)
weather_data_raw = requests.get(weather_data)
weather_data_pro = json.loads(weather_data_raw.text)

for temp_day in weather_data_pro["result"]:
    temp_data.append((temp_day["temp"]["mean"]))

for hum_day in weather_data_pro["result"]:
    hum_graph.append(hum_day["humidity"]["mean"])

temp_graph = [round((temp_day - 273.15), 2) for temp_day in temp_data]


size_graph, ax_1 = plt.subplots()
ax_1.plot(days_graph, temp_graph)
ax_1.set_xlabel("Average Temperature Versus Average Humidity (" + zip_input.city + ")")
ax_1.set_ylabel('Temperature(C)', color='tab:blue')
ax_1.grid(True)
ax_2 = ax_1.twinx()
ax_2.plot(days_graph, hum_graph, color='tab:orange')
ax_2.set_ylim([0, 100])
ax_2.set_ylabel('Humidity(%)', color='tab:orange')
size_graph.tight_layout()
plt.show()
