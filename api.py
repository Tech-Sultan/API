import requests

api = 'https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = input('Enter your city: ')
url = api + city

jason_data = requests.get(url).json()
formatted_data = jason_data['weather'][0]['description']
print(formatted_data)
