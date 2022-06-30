from pip import main
import requests

api_key='f1ad3ba3e9c8066ace83a7b31c3e8d13'
user_input=input("Enter the name of the city you wish : ")
weather_data=requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod']=='404':
    print("NO City Found")
else:
    weather=weather_data.json()['weather'][0]['main']
    temp=round(weather_data.json()['main']['temp'])
    
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is : {temp} °F")