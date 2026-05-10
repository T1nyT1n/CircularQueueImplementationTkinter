# == ИМПОРТ ==

from tkinter.messagebox import showinfo, showerror # Поп-апы
import sys
import importlib
import webbrowser # Для открытия ссылки на репозиторий в браузере
import config as c

# == ОПРЕДЕЛИТЬ МОДУЛЬ ОЧЕРЕДИ ==

def ExitOnWrongUsage():
    print("""Использование: python3 main.py <аргумент>
Аргументы:
    P — модуль Python. 
    C — модуль C++.""")
    sys.exit(1)

if len(sys.argv) < 2:
    ExitOnWrongUsage()

# Импорт очереди
if sys.argv[1] == "P":
    q = importlib.import_module('py_queue')
elif sys.argv[1] == "C":
    ExitOnWrongUsage() # TODO: заменить, когда будет создан C++ модуль
else:
    ExitOnWrongUsage()

# Проверка на корректное выполнение функции из модуля
def ExecuteDangerousOp(res: int):
    if res == -1:
        showerror(message="Что-то пошло не так... Обычно вы не должны" \
            " видеть это сообщение. Если вы это читаете — в программе ошибка!")
    else:
        UpdateRead()
    return res

# Проверка на число в формах для ввода

def ValidateIntString(value):
    """
    Проверяет строку value.
    True, если содержит только int.
    False, если содержит что-либо другое.
    """
    if value == "" or value == "-":
        return True
    if value[0] == "-":
        return value[1:].isdigit()
    return value.isdigit()

# == ВСТАВКА ==

def PushElement():
    data_to_push = c.E_PUSH_ENTRY_DATA.get()
    res = q.PushElement(data_to_push)
    if res == -1:
        showerror("Что-то пошло не так...")
    else:
        UpdateRead()

# == ЧТЕНИЕ == 

def UpdateRead(): # выполнять после каждой операции над очередью!
    data = q.ReadElement()
    if data != None:
        c.L_TOP_NUMBER.config(text = str(data))
    else:
        c.L_TOP_NUMBER.config(text = "Пусто!")
        
# == УДАЛИТЬ ==

def PopElement():
    if q.EmptyQueue() != True:
        res = ExecuteDangerousOp(q.PopElement())
        showinfo(message=f"Удалён элемент: {res}")
    else:
        showerror(message="Невозможно удалить элемент из пустой очереди." \
            " Поместите хотя бы один элемент в очередь.")

# == ОЧИСТКА ОЧЕРЕДИ ==

def ClearQueue():
    if q.EmptyQueue() != True:
        res = ExecuteDangerousOp(q.ClearQueue())
        showinfo(message=f"Очередь очищена! Удалено элементов: {res}")
    else:
        showerror(message="Невозможно очистить пустую очередь. Поместите" \
            " хотя бы один элемент в очередь.")

# == ВСЕ ЭЛЕМЕНТЫ ==

def ShowAllElements():
    if q.EmptyQueue() != True:
        res = ExecuteDangerousOp(q.ShowAllElements())
        showinfo(message=f"Все элементы в очереди: {res}")
    else:
        showerror(message="Невозможно очистить пустую очередь. Поместите" \
            " хотя бы один элемент в очередь.")

# == МЕНЮ ==

def QuitProgram():
    """
    Закрывает программу.
    """
    c.W_MAIN.quit()

def OpenGitHubRepo():
    """
    Открывает страницу Git-репозитория программы в веб-браузере.
    """
    # TODO: заменить на ссылку репозитория.
    webbrowser.open("https://github.com/")

def ShowAboutScreen():
    """
    Показывает поп-ап с информацией о программе.
    """
    showinfo(title="О программе", message="Программа для демонстрации работы" \
        " с циклической очередью.")