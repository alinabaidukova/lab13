from tkinter import *
import requests
import webbrowser
import folium   # для работы с картами

def get_weather():
    city = cityField.get()  # получение данных от пользователя

    key = '61487bfbb99bc82551f3beaaaab570f5'
    url = 'http://api.openweathermap.org/data/2.5/weather'  # ссылка для получения всех данных в json
    params = {'APPID': key, 'q': city, 'units': 'metric'}  # ключ, город, шкала измерения
    result = requests.get(url, params=params)  # отправление запроса
    weather = result.json()  # получение json

    lat = weather['coord']['lat']   # данные о широте, долготе, названии города и температуре
    lon = weather['coord']['lon']
    name = weather['name']
    temp = weather['main']['temp']

    map = folium.Map(location=[lat, lon], zoom_start=12)  # folium.Map-создание объект-карты по долготе и широте, zoom_start-увеличение карты
    folium.Marker(location=[lat, lon], tooltip=name + ': ' + str(temp) + '°C').add_to(map)    # создание маркера, tooltip-название и температура у маркера, add_to(map)-добавление маркера

    map.save('map.html')

    webbrowser.open('map.html') # сохранение карты в html

root = Tk()
root['bg'] = '#C3E4EB'
root.title('Карта с погодой')
root.geometry('400x600')
root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ECECEB', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

cityField = Entry(frame_top, bg='white', font=30)  # поле для ввода города
cityField.pack()  # Размещение поля

btn = Button(frame_top, text='Посмотреть погоду', bg='#EDEFD6',
             command=get_weather)  # Кнопка, при нажатии срабатывает метод "get_weather"
btn.pack()

root.mainloop()