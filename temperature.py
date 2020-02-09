import requests
from envirophat import weather
from settings import device_name, temperature_endpoint

temp = weather.temperature

json_data = {
    "temperature": temp,
    "device": device_name
}

response = requests.put(
    url=temperature_endpoint,
    json=json_data
)


