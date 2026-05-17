# If response code is 1XX: HOLD ON
# If response code is 2XX: HERE YOU GO
# If response code is 3XX: GO AWAY
# If response code is 4XX: YOU SCREWED UP
# If response code is 5XX: I SCREWED UP (for more you can visit httpstatuses.com)

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

import requests
from datetime import datetime

MY_LAT = 23.526163
MY_LNG = 72.360352

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LNG,
    "formatted" : 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now)