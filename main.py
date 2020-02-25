import sys
import datetime
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtCore import QFile
from PySide2.QtGui import QPixmap
from uidesign import Ui_MainWindow
from city import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

ob = window.ui

ob.todayLabel4.setWordWrap(True)
ob.tomorrowLabel4.setWordWrap(True)

listTempLabel = [
    ob.temp0_5,
    ob.temp3_5,
    ob.temp6_5,
    ob.temp9_5,
    ob.temp12_5,
    ob.temp15_5,
    ob.temp18_5,
    ob.temp21_5,
    ob.temp0_4,
    ob.temp3_4,
    ob.temp6_4,
    ob.temp9_4,
    ob.temp12_4,
    ob.temp15_4,
    ob.temp18_4,
    ob.temp21_4,
]
listWindLabel = [
    ob.wind0_5,
    ob.wind3_5,
    ob.wind6_5,
    ob.wind9_5,
    ob.wind12_5,
    ob.wind15_5,
    ob.wind18_5,
    ob.wind21_5,
    ob.wind0_4,
    ob.wind3_4,
    ob.wind6_4,
    ob.wind9_4,
    ob.wind12_4,
    ob.wind15_4,
    ob.wind18_4,
    ob.wind21_4
]

listPictureLabel = [
    ob.lab0_5,
    ob.lab3_5,
    ob.lab6_5,
    ob.lab9_5,
    ob.lab12_5,
    ob.lab15_5,
    ob.lab18_5,
    ob.lab21_5,
    ob.lab0_4,
    ob.lab3_4,
    ob.lab6_4,
    ob.lab9_4,
    ob.lab12_4,
    ob.lab15_4,
    ob.lab18_4,
    ob.lab21_4
]

dictPicture = {
    'Partly Cloudy' : 'sunWithCloud.png',
    'Mostly Cloudy' : 'cloud.png',
    'Overcast' : 'cloud.png',
    'Possible Drizzle' : 'rain.png',
    'Possible Light Rain' : 'rain.png',
    'Clear' : 'clear.png',
    'partly-cloudy-day' : 'cloud.png',
    'clear-day' : 'clear.png',
    'snow' : 'snow.png',
    'Snow' : 'snow.png',
    'rain' : 'rain.png',
    'Possible Flurries' : 'snow.png',
    'Foggy' : 'fog.png',
    'Possible Light Snow' : 'snow.png',
    'fog' : 'fog.png',
    'Light Rain' : 'rain.png',
    'Drizzle' : 'rain.png',
    'cloudy' : 'cloud.png'
}

def avgList(lt):
    sum = 0
    for x in range(0,8):
        sum += lt[x]
    return round(sum/8,2)


def fillLabel(Town):
    temp2day = Town.getTodayWeatherTemp() # list with all 16 temp
    wind2day = Town.getTodayWeatherWind() # list with all 16 wind
    summary2day = Town.getTodayWeatherSummary() # list with all 16 summary
    daySummary = Town.getDaySummary() # List with 2 summary (today, tomorrow)
    dayPicture = Town.getDayIcon()

    ob.todayLabel2.setText(str(avgList(temp2day))+ '°')
    ob.tomorrowLabel2.setText(str(avgList(temp2day[8:])) + '°')
    ob.tomorrowLabel4.setText(daySummary[1])
    ob.todayLabel4.setText(daySummary[0])
    ob.todayLabel3.setPixmap(QPixmap(u'img/' + str(dictPicture[dayPicture[0]])).scaled(50,50))
    ob.tomorrowLabel3.setPixmap(QPixmap(u'img/' + str(dictPicture[dayPicture[1]])).scaled(50,50))

    d = 0
    for k in range(0,16):
        listTempLabel[d].setText(str(temp2day[k]) + '°')
        listWindLabel[d].setText(str(wind2day[k]))
        listPictureLabel[d].setPixmap(QPixmap(u'img/' + str(dictPicture[summary2day[k]])).scaled(50,50))
        d = d + 1 
        

def loadWeather():
    town = ob.currentTownLabel.text().split(' ')[2]    
    Town = City_Weather(town)
    fillLabel(Town)

ob.todayLabel1.setText(str(datetime.date.today()) + '\nСегодня')
ob.tomorrowLabel1.setText(str(datetime.date.today() + datetime.timedelta(days=1)) + '\nЗавтра')

ob.currentTownLabel.setText('Выбранный город: Минск')

loadWeather()

ob.brestRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Брест'))
ob.pinskRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Пинск'))
ob.baranovichiRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Барановичи'))

ob.vitebskRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Витебск'))
ob.polotskRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Полоцк'))
ob.orshaRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Орша'))

ob.gomelRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Гомель'))
ob.turovRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Туров'))
ob.mozirRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Мозырь'))

ob.grodnoRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Гродно'))
ob.lidaRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Лида'))
ob.volkovyskRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Волковыск'))

ob.minskRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Минск'))
ob.borisobRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Борисов'))
ob.soligorskRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Солигорск'))

ob.mogilevRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Могилёв'))
ob.bobruyskRB.clicked.connect(lambda: ob.currentTownLabel.setText('Выбранный город: Бобруйск'))

ob.pushButton.clicked.connect(loadWeather)

sys.exit(app.exec_())