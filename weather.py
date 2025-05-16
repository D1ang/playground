class WeatherModel:
    """
    A Basic weather model with stats

    return:
        temprature (str)
        humidity (str)
        wind_speed (str)
    """
    def __init__(self, temperature, humidity, wind_speed):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed

    def get_weather_info(self):
        return {
            "temperature": self.temperature,
            "humidity": self.humidity,
            "wind_speed": self.wind_speed
        }


weather = WeatherModel(5, 6, 8)
print(weather.get_weather_info())








# class WeatherView:
#     def display_weather(self, weather_info):
#         print(f"Temperature: {weather_info['temperature']}°C")
#         print(f"Humidity: {weather_info['humidity']}%")
#         print(f"Wind Speed: {weather_info['wind_speed']} km/h")


# class WeatherController:
#     def __init__(self, model, view):
#         self.model = model
#         self.view = view

#     def update_weather(self, temperature, humidity, wind_speed):
#         self.model.temperature = temperature
#         self.model.humidity = humidity
#         self.model.wind_speed = wind_speed

#     def show_weather(self):
#         weather_info = self.model.get_weather_info()
#         self.view.display_weather(weather_info)

# Example usage
