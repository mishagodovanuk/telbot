from core import config
from urllib import request, error
import telebot, os, openai, json, sys


class TelBot(telebot.TeleBot):
    bot_token = None
    aiBot = None

    def __init__(self, token):
        # TODO replace conf_dict var by dic()
        super().__init__(token)
        openai.organization = config.oai_org
        openai.api_key = config.oai_api_key
        openai.Model.list()

    def bot_answer_message(self, message):
        answer = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message.text}
            ]
        )
        self.send_message(message.chat.id, answer.choices[0].message.content, None, None, None, 'MARKDOWN')

    def bot_photo(self, message):
        # print(message.photo)
        self.send_message(message.chat.id, 'we recieve your photo')

    def bot_repeat_message(self, message):
        self.send_message(message.chat.id, message.text)

    def bot_get_weather(self, message):
        mess = None
        city_m = message.text.replace('/weather ', '')
        city = city_m.replace(' ', '+')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.weather_api_key}&units=metric"

        try:
            response = request.urlopen(url)
            data = response.read()

            try:
                weather = json.loads(data)
                mess = self.conbine_weather_message(city_m, weather)

            except json.JSONDecodeError:
                mess = "Couldn't read the server response."

        except error.HTTPError as http_error:
            if http_error.code == 401:  # 401 - Unauthorized
                mess = "Access denied. Check your API key."
            elif http_error.code == 404:  # 404 - Not Found
                mess = "Can't find weather data for this city."
            else:
                mess = f"Something went wrong... ({http_error.code})"

        self.send_message(message.chat.id, mess)

    def conbine_weather_message(self, city, weather):
        desc_data = weather['weather'][0]['description']
        temp_b_data = f"(Avarage {weather['main']['temp']}°C)"
        temp_min_data = f"(Min {weather['main']['temp_min']}°C)"
        temp_max_data = f"(Max {weather['main']['temp_max']}°C)"
        pressure = f"(Pressure {weather['main']['pressure']} Pa)"
        humidity = f"(Humidity {weather['main']['humidity']}%)"
        wind_speed = f"(Wind Speed {weather['wind']['speed']} m/s)"
        # set up overall info
        mess = f"🏙 {city} \n \n 💡 {desc_data} \n \n 🌡 {temp_b_data} \n 🌡 {temp_min_data} \n 🌡 {temp_max_data} \n \n 🌍 {pressure} \n \n  💦 {humidity} \n \n 💨 {wind_speed}"
        return mess
