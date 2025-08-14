import tkinter as tk
from tkinter import messagebox
import requests

def weather():
    city = cityentry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    api_key = "a4b1aa8a5392716b9e251653ca409922"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            messagebox.showerror("API Error", f"{response.status_code}: {response.json()['message']}")
            return

        data = response.json()
        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description'].capitalize()
        result = f"City: {city}\nTemperature: {temp} °C\nHumidity: {humidity}%\nCondition: {condition}"
        result_label.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("WEATHER APP 2025")
root.geometry("250x250")
root.resizable(False, False)
tk.Label(root, text="ENTER CITY NAME:", font=("Arial", 14)).pack(pady=10)
cityentry = tk.Entry(root, font=("Arial", 12))
cityentry.pack(pady=5)
tk.Button(root, text="Get Weather", font=("Arial", 12), command=weather).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)
root.mainloop()
