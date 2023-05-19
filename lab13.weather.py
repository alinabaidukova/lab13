from tkinter import *
import requests
from tkinter import messagebox

root=Tk()
root['bg'] = '#C3E4EB'
root.title('Приложение погоды')
root.geometry('400x600')
root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ECECEB', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#ECECEB', bd=3)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

def get_weather():
    city = cityField.get()  #получение данных от пользователя

    key = '61487bfbb99bc82551f3beaaaab570f5'
    url = 'http://api.openweathermap.org/data/2.5/weather'  #ссылка для получения всех данных в json
    params = {'APPID': key, 'q': city, 'units': 'metric'}   #ключ, город, шкала измерения
    result = requests.get(url, params=params)   #отправление запроса
    weather = result.json() #получение json

    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}' #вывод данных о погоде


cityField = Entry(frame_top, bg='white', font=30)   #поле для ввода города
cityField.pack()  # Размещение поля

btn = Button(frame_top, text='Посмотреть погоду', bg='#EDEFD6', command=get_weather)    #Кнопка, при нажатии срабатывает метод "get_weather"
btn.pack()


info = Label(frame_bottom, text='Погодная информация', bg='#A8B3DA', font=50)   #информация о погоде
info.pack()

"""messagebox.showerror(title='Окно с ошибкой', message= 'Ошибка!!!')"""

# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()