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
    ctypes = importlib.import_module('ctypes')
    platform = importlib.import_module('platform')
    if platform.system() == 'Linux':
        q = ctypes.CDLL('./libqueue.so')
    else: # TODO: поменять на elif
        q = ctypes.CDLL('./libqueue.dll')
    head = ctypes.c_void_p.in_dll(q, 'head')
    tail = ctypes.c_void_p.in_dll(q, 'tail')
    count = ctypes.c_int.in_dll(q, 'count')
    q.EmptyQueue.restype = ctypes.c_bool
    q.ReadElement.restype = ctypes.c_int
    q.PushElement.argtypes = [ctypes.c_int]
    q.PopElement.restype = ctypes.c_int
    q.ClearQueue.restype = ctypes.c_int
    q.ShowAllElements.restype = ctypes.c_void_p
    q.RemoveElementsByCondition.argtypes = [ctypes.c_int, ctypes.c_int]
    q.RemoveElementsByCondition.restype = ctypes.c_int
    q.FreeCString.argtypes = [ctypes.c_void_p]
else:
    ExitOnWrongUsage()

# Проверка на корректное выполнение функции из модуля
def ExecuteDangerousOp(res):
    if res == -1:
        showerror(message="Что-то пошло не так... Обычно вы не должны" \
            " видеть это сообщение. Если вы это читаете — в программе" \
            " ошибка!")
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
    res = 0
    if data_to_push != "":
        res = q.PushElement(int(data_to_push))
    if res == -1:
        showerror("Что-то пошло не так...")
    else:
        UpdateRead()

# == ЧТЕНИЕ == 

def UpdateRead(): # выполнять после каждой операции над очередью!
    if q.EmptyQueue():
        c.L_TOP_NUMBER.config(text = "Пусто!")
    else:
        data = q.ReadElement()
        c.L_TOP_NUMBER.config(text = str(data))
        
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
        ptr = q.ShowAllElements()
        if sys.argv[1] == 'C':
            s = ctypes.cast(ptr, ctypes.c_char_p).value.decode('utf-8')
            showinfo(message=f"Все элементы в очереди: {s}")
            q.FreeCString(ptr)
        else:
            showinfo(message=f"Все элементы в очереди: {ptr}")
    else:
        showerror(message="Невозможно показать пустую очередь. Поместите" \
            " хотя бы один элемент в очередь.")
        
# == УДАЛИТЬ С УСЛОВИЕМ ==

def RemoveElementsByCondition():
    condition = int(c.COMPARING_SIGN.get())
    num = int(c.E_CONDITION_NUMBER.get())
    q.RemoveElementsByCondition(condition, num)
    UpdateRead()

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
    webbrowser.open(\
        "https://github.com/T1nyT1n/CircularQueueImplementationTkinter")

def ShowAboutScreen():
    """
    Показывает поп-ап с информацией о программе.
    """
    showinfo(title="О программе", message="Программа для демонстрации" \
        " работы с циклической очередью.")