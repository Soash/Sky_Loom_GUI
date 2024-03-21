import tkinter as tk
import requests
import threading

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Sky_Loom_GUI")
        master.geometry("400x400")

        self.location_label = tk.Label(master, text="Enter Location:")
        self.location_label.pack()

        self.location_entry = tk.Entry(master)
        self.location_entry.pack()

        self.submit_button = tk.Button(master, text="Get Weather", command=self.fetch_weather)
        self.submit_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def fetch_weather(self):
        location = self.location_entry.get()
        if location:
            self.submit_button.config(state="disabled")
            self.result_label.config(text="Loading...")
            threading.Thread(target=self.get_weather_data, args=(location,)).start()

    def get_weather_data(self, location):
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=fb0a12bf21012a1080dc82c63b058a8c"
            response = requests.get(url)
            data = response.json()

            temperature = data['main']['temp']
            temperature_celsius = temperature - 273.15  

            result_text = f"Temperature: {temperature_celsius:.2f} °C"
            self.result_label.config(text=result_text)
        except Exception as e:
            self.result_label.config(text="Error fetching weather data :(")
        finally:
            self.submit_button.config(state="normal")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
