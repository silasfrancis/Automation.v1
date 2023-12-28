import requests

API_KEY = "b174e98b970fab142e4510e44afbd8f1"
BASE_URL= "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
     data = response.json()
     #print(data)
     weather = data['weather'][0]['description']
     temperature = round(data['main']['temp'] - 273, 2)
     print("Weather:", weather)
     print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")

