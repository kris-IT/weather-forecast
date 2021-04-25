# Импортируем все из библиотеки TKinter
from tkinter import *

# Эта библиотека нужна для работы с отправкой URL запросов
import requests

# Окно приложения
root = Tk()
# Эта функция срабатывает при нажатии на кнопку "Посмотреть погоду"
def get_weather():
    # Получаем данные от пользователя
    city = cityField.get()
    key = '764918519e3575151c5923a7a0f58dd0'
    # ссылка, с которой мы получим все данные в формате JSON
    url = 'http://api.openweathermap.org/data/2.5/weather'
    # Дополнительные парамтеры (Ключ, город введенный пользователем и единицины измерения - metric означает Цельсий)
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    # Отправляем запрос по определенному URL
    result = requests.get(url, params=params)
    # Получаем JSON ответ по этому URL
    weather = result.json()

    # Полученные данные добавляем в текстовую надпись для отображения клиенту
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'

# Настройки главного окна
# Указываем фоновый цвет
root['bg'] = '#fafafa'
# Указываем название окна
root.title('Погода')
# Прозрачность окна
root.wm_attributes('-alpha', 0.9)
# Указываем размеры окна
root.geometry('300x250')
# Делаем невозможным менять размеры окна
root.resizable(width=False, height=False)

# Создаем первый фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
frame_top = Frame(root, bg='#535353', bd=5)
# Также указываем его расположение
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

# Второй фрейм
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

# Создаем текстовое поле для получения данных от клиента
cityField = Entry(frame_top, bg='#bcbcbc', font=30)
cityField.pack()

# Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()

# Создаем текстовую надпись, в которую будет выводиться информация о погоде
info = Label(frame_bottom, text='Вывод информации', bg='#ffb700', font=80)
info.pack()

# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()