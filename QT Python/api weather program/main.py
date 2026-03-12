import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()

        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addWidget(self.city_label)
        hbox.addWidget(self.city_input)
        hbox.addWidget(self.get_weather_button)

        vbox.addLayout(hbox)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # it is id not class
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.emoji_label.setObjectName("emoji_label")
        self.temperature_label.setObjectName("temperature_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton { font-family: calibri; }
            QLabel#city_label { font-size: 20px; font-style: italic; }
            QLineEdit#city_input { font-size: 20px; }
            QPushButton#get_weather_button { font-size: 18px; font-weight: bold; padding: 4px 15px;}
            QLabel#temperature_label { font-size: 30px; font-weight: bold; }
            QLabel#emoji_label { font-size: 70px; font-family: Segoe UI emoji; }
            QLabel#description_label { font-size: 20px; font-weight: bold; }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "01c13f02a353adedab13f4755780f4e0"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data['cod'] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error(
                        "Internal server error:\nPlease try again later")
                case 501:
                    self.display_error(
                        "Bad Gateaway:\nInvalid response from the server")
                case 502:
                    self.display_error("Service Unavailable:\nServer is down")
                case 503:
                    self.display_error(
                        "Gateaway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP ERROR {http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error(
                "Connection error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setText(message)
        self.temperature_label.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: red;")
        self.emoji_label.clear()
        self.description_label.clear()

    @staticmethod
    def get_temperature_color(temperature):
        ranges = {
            range(-100, 1): "#1b15cf",
            range(0, 11): "#433fbf",
            range(10, 26): "#ba9304"
        }

        for key, value in ranges.items():
            if temperature in key:
                return value

        return "#db4809" if temperature > 25 else ""

    @staticmethod
    def get_weather_emoji(weather_id):
        ranges = {
            range(200, 233): "⛈️",
            range(300, 322): "🌦️",
            range(500, 532): "🌧️",
            range(600, 623): "❄️",
            range(700, 782): "🌪️",
            range(801, 805): "☁️"
        }

        for k, emoji in ranges.items():
            if weather_id in k:
                return emoji

        return "☀️" if weather_id == 800 else ""

    def display_weather(self, data):
        temperature = data["main"]["temp"] - 273.15
        print(data)

        weather_description = data["weather"][0]["description"]
        temperature_color = self.get_temperature_color(temperature)

        weather_id = data["weather"][0]["id"]
        weather_emoji = self.get_weather_emoji(weather_id)

        self.temperature_label.setText(f"{temperature:.1f}°C")
        self.temperature_label.setStyleSheet(
            f"color: {temperature_color}; font-size: 30px;")
        self.description_label.setText(weather_description.capitalize())
        self.emoji_label.setText(weather_emoji)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
