import requests
from key import key
from googletrans import Translator

translator = Translator()

translate_town = {
    'Брест': 'Brest',
    'Барановичи': 'Podstazhynki',  # Барановичи
    'Пинск': 'Pinsk',
    'Витебск': 'Haradok',  # Витебск
    'Полоцк': 'Disna',  # Полоцк
    'Орша': 'Orhsa',
    'Гомель': 'Gomel',
    'Туров': 'Zytkowicze',  # Туров
    'Мозырь': 'Mazyr',
    'Гродно': 'Hrodna',
    'Лида': 'Lida',
    'Волковыск': 'Vawkavysk',
    'Минск': 'Minsk',
    'Солигорск': 'Salihorsk',
    'Борисов': 'Novo Yanchino',  # Борисов
    'Могилёв': 'Brakovo',  # Могилёв
    'Бобруйск': 'Podrechye',  # Бобруйск
}

town_dict = {
    'Brest': '51.953068,23.675537',
    'Podstazhynki': '53.089076,26.032104',  # Барановичи
    'Pinsk': '51.953068,26.048584',
    'Haradok': '55.186709,30.261841',  # Витебск
    'Disna': '55.523967,28.646851',  # Полоцк
    'Orhsa': '54.484400,30.404663',
    'Gomel': '52.410797,31.041870',
    'Zytkowicze': '52.060935,27.976685',  # Туров
    'Mazyr': '52.027149,29.262085',
    'Hrodna': '53.711339,23.812866',
    'Lida': '53.882083,25.302887',
    'Vawkavysk': '53.154388,24.441147',
    'Minsk': '53.880059,27.592163',
    'Salihorsk': '52.771201,27.515259',
    'Novo Yanchino': '54.196190,28.504028',  # Борисов
    'Brakovo': '53.893010,30.371704',  # Могилёв
    'Podrechye': '53.122054,29.218140'  # Бобруйск
}

DARKSKY_API_KEY = key


class City_Weather (object):
    def __init__(self, name):
        self.cityName = translate_town[name]
        self.cityCoord = town_dict[self.cityName]
        self.__api_conditions_url = "https://api.darksky.net/forecast/" + \
            DARKSKY_API_KEY + "/" + self.cityCoord + "?units=auto"
        self.__request = requests.get(self.__api_conditions_url)
        self.__weatherDict = eval(self.__request.text)

    def getTodayWeatherTemp(self):
        tempDay = []
        for k in range(0,47,3):
            tempDay.append(self.__weatherDict['hourly']['data'][k]['temperature'])
        return tempDay
        
    def getTodayWeatherSummary(self):
        summaryDay = []
        for k in range(0,47,3):
            summaryDay.append(self.__weatherDict['hourly']['data'][k]['summary'])
        return summaryDay
        
    def getTodayWeatherWind(self):
        windDay = []
        for k in range(0,47,3):
            windDay.append(self.__weatherDict['hourly']['data'][k]['windSpeed'])
        return windDay

    def getDaySummary(self):
        summaryDay = []
        summaryDay.append(str(translator.translate(self.__weatherDict['daily']['data'][0]['summary'], dest='ru').text))
        summaryDay.append(str(translator.translate(self.__weatherDict['daily']['data'][1]['summary'], dest='ru').text))
        return summaryDay

    def getDayIcon(self):
        dayIcon = []
        dayIcon.append(self.__weatherDict['daily']['data'][0]['icon'])
        dayIcon.append(self.__weatherDict['daily']['data'][1]['icon'])
        return dayIcon