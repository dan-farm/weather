from dotenv import load_dotenv
import os
import requests
from tkinter import *

load_dotenv()

key = os.getenv("KEY") # Store key in .env file as KEY=your_api_key_here
city = os.getenv("CITY") # Store city in .env file as CITY=your_city_here
root = Tk()
T = Text(root, height = 2, width = 30)
T.pack()


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Unable to fetch weather data for {city}. Status code: {response.status_code}")
        return
    else:
        data = response.json()
        description = (data["weather"][0]["description"]).capitalize()
        print(f'{data["name"]}: {data["main"]["temp"]}°C')
        print(f"Weather: {description}")
        
        T.insert(END, f'{data["name"]}: {data["main"]["temp"]}°C\n')
        T.insert(END, f"Weather: {description}\n")
     #   T.wm_attributes("-topmost", True)
        mainloop()

def main():
    get_weather(city)

if __name__ == "__main__":
    main()