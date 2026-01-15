from tkinter import *
import os

root = Tk()
root.title("Управление устройствами")
root.geometry("600x400")

# Функции для меню "Изображение" (с фото)
def show_image(filename, title):
    new_window = Toplevel(root)
    new_window.title(title)

    if os.path.exists(filename):
        try:
            img = PhotoImage(file=filename)
            label = Label(new_window, image=img)
            label.image = img  # сохраняем ссылку на изображение
            label.pack()
        except:
            Label(new_window, text=f"Ошибка загрузки {filename}").pack()
    else:
        Label(new_window, text=f"Файл {filename} не найден").pack()

def show_camera_image():
    show_image("1.png", "Изображение камеры")

def show_microcontroller_image():
    show_image("2.png", "Изображение микроконтроллера")

def show_motion_sensor_image():
    show_image("3.png", "Изображение датчика движения")

def show_thermometer_image():
    show_image("4.png", "Изображение термометра")

# Функции для меню "Характеристики" (без фото)
def show_camera_info():
    new_window = Toplevel(root)
    new_window.title("Характеристики камеры")
    text = "Камера:\nРазрешение: 1080p\nFPS: 30\nУгол обзора: 90°"
    Label(new_window, text=text).pack()

def show_microcontroller_info():
    new_window = Toplevel(root)
    new_window.title("Характеристики микроконтроллера")
    text = "Микроконтроллер:\nМодель: Arduino\nПамять: 32KB\nПины: 14"
    Label(new_window, text=text).pack()

def show_motion_sensor_info():
    new_window = Toplevel(root)
    new_window.title("Характеристики датчика движения")
    text = "Датчик движения:\nДальность: 7м\nУгол: 120°\nЗадержка: 5-300с"
    Label(new_window, text=text).pack()

def show_thermometer_info():
    new_window = Toplevel(root)
    new_window.title("Характеристики термометра")
    text = "Термометр:\nДиапазон: -55...+125°C\nТочность: ±0.5°C\nИнтерфейс: 1-Wire"
    Label(new_window, text=text).pack()

# Функции для меню "Функции"
def show_camera_functions():
    new_window = Toplevel(root)
    new_window.title("Функции камер")
    text = "1. Объектив:\n   - Фокусировка\n   - Зум\n\n2. Матрица:\n   - Запись видео\n   - Фотосъемка"
    Label(new_window, text=text).pack()

def show_microcontroller_functions():
    new_window = Toplevel(root)
    new_window.title("Функции микроконтроллеров")
    text = "1. АЦП:\n   - Чтение датчиков\n   - Преобразование\n\n2. ШИМ:\n   - Управление моторами\n   - Регулировка"
    Label(new_window, text=text).pack()

def show_sensor_functions():
    new_window = Toplevel(root)
    new_window.title("Функции датчиков движения")
    text = "1. PIR элемент:\n   - Обнаружение\n   - ИК-излучение\n\n2. Линза:\n   - Фокусировка\n   - Зона"
    Label(new_window, text=text).pack()

def show_thermometer_functions():
    new_window = Toplevel(root)
    new_window.title("Функции термометров")
    text = "1. Терморезистор:\n   - Измерение\n   - Точность\n\n2. Интерфейс:\n   - 1-Wire\n   - Подключение"
    Label(new_window, text=text).pack()

# Создание меню
mainmenu = Menu(root)
root.config(menu=mainmenu)

# Меню "Файл"
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Выход", command=root.quit)

# Меню "Изображение"
imgmenu = Menu(mainmenu, tearoff=0)
imgmenu.add_command(label="Камера", command=show_camera_image)
imgmenu.add_command(label="Микроконтроллер", command=show_microcontroller_image)
imgmenu.add_command(label="Датчик движения", command=show_motion_sensor_image)
imgmenu.add_command(label="Термометр", command=show_thermometer_image)

# Меню "Характеристики"
charmenu = Menu(mainmenu, tearoff=0)
charmenu.add_command(label="Камера", command=show_camera_info)
charmenu.add_command(label="Микроконтроллер", command=show_microcontroller_info)
charmenu.add_command(label="Датчик движения", command=show_motion_sensor_info)
charmenu.add_command(label="Термометр", command=show_thermometer_info)

# Меню "Функции"
funcmenu = Menu(mainmenu, tearoff=0)
funcmenu.add_command(label="Камеры", command=show_camera_functions)
funcmenu.add_command(label="Микроконтроллеры", command=show_microcontroller_functions)
funcmenu.add_command(label="Датчики движения", command=show_sensor_functions)
funcmenu.add_command(label="Термометры", command=show_thermometer_functions)

# Добавление меню
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Изображение", menu=imgmenu)
mainmenu.add_cascade(label="Характеристики", menu=charmenu)
mainmenu.add_cascade(label="Функции", menu=funcmenu)


root.mainloop()