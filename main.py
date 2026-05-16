# == ИМПОРТ ==

import tkinter as t # Кроссплатформенный UI
import business
import config as c # Общие переменные

# == ОСНОВНОЕ ОКНО ==

c.W_MAIN = t.Tk()
c.W_MAIN.title("Циклическая очередь")
c.W_MAIN.geometry('750x500+300+300')
c.W_MAIN.resizable(False, False)
validate_int = (c.W_MAIN.register(business.ValidateIntString), "%P")

# — СОЗДАНИЕ ВИДЖЕТОВ —

# Вставка

lf_push = t.LabelFrame(c.W_MAIN, text="Вставить элемент")
l_enter_number = t.Label(lf_push, text="Введите целое число для добавления в " \
    "очередь:")
c.E_PUSH_ENTRY_DATA = t.Entry(lf_push, validate="key", \
    validatecommand=validate_int)
b_push = t.Button(lf_push, text="Вставить", bg="lightgreen", \
    command=business.PushElement)

# Чтение

f_read = t.Frame()
l_read_description = t.Label(f_read, text="Элемент в начале очереди")
c.L_TOP_NUMBER = t.Label(f_read, text="-123456", font=("Consolas", 30))
business.UpdateRead()

# Удалить

f_pop = t.Frame()
l_about_pop = t.Label(f_pop, text="Удалить один элемент из начала очереди")
b_pop = t.Button(f_pop, text="Удалить", bg="lightcoral", \
    command=business.PopElement)

# Очистить

f_clear = t.Frame()
b_clear = t.Button(f_clear, text="Очистить очередь", bg="firebrick1", \
    command=business.ClearQueue)

# Показать все элементы

f_showall = t.Frame()
b_showall = t.Button(f_showall, text="Показать все", bg="LightSteelBlue", \
    command=business.ShowAllElements)

# Убрать элементы по условию

c.COMPARING_SIGN = t.IntVar()
c.COMPARING_SIGN.set(0)

lf_remove_by_condition = t.LabelFrame(c.W_MAIN, text="Удалить элементы по" \
    " условию")
c.E_CONDITION_NUMBER = t.Entry(lf_remove_by_condition, validate="key", \
    validatecommand=validate_int)
rb_less = t.Radiobutton(lf_remove_by_condition, text="<", \
    variable=c.COMPARING_SIGN, value=0)
rb_more = t.Radiobutton(lf_remove_by_condition, text=">", \
    variable=c.COMPARING_SIGN, value=1)
rb_equals = t.Radiobutton(lf_remove_by_condition, text="=", \
    variable=c.COMPARING_SIGN, value=2)
b_remove = t.Button(lf_remove_by_condition, text="Удалить", \
    bg="lightyellow", command=business.RemoveElementsByCondition)

# — РАЗМЕЩЕНИЕ ВИДЖЕТОВ —

# Вставка

lf_push.pack()
l_enter_number.pack(padx=5)
c.E_PUSH_ENTRY_DATA.pack(side=t.LEFT, padx=10, expand=True, fill="x")
b_push.pack(side=t.RIGHT, padx=5, pady=5)

# Чтение

f_read.pack()
l_read_description.pack()
c.L_TOP_NUMBER.pack()

# Удалить

f_pop.pack()
l_about_pop.pack()
b_pop.pack()

# Очистить

f_clear.pack()
b_clear.pack()

# Показать все элементы

f_showall.pack()
b_showall.pack()

# Убрать элементы по условию

lf_remove_by_condition.pack()
c.E_CONDITION_NUMBER.pack(side=t.TOP, expand=True, fill="both", padx=5)
rb_less.pack(side=t.LEFT, padx=5)
rb_more.pack(side=t.LEFT, padx=5)
rb_equals.pack(side=t.LEFT, padx=5)
b_remove.pack(side=t.RIGHT, padx=5, pady=5)

# == СТРОКА МЕНЮ ==

m_bar = t.Menu()

m_file = t.Menu(m_bar, tearoff=0)
m_file.add_command(label="Выйти", command=business.QuitProgram)

m_help = t.Menu(m_bar, tearoff=0)
m_help.add_command(label="Просмотреть репозиторий на GitHub", \
    command=business.OpenGitHubRepo)
m_help.add_command(label="О программе", command=business.ShowAboutScreen)

m_bar.add_cascade(label="Файл", menu=m_file)
m_bar.add_cascade(label="Справка", menu=m_help)

c.W_MAIN.config(menu = m_bar)

# == ЦИКЛ ОБРАБОТКИ СОБЫТИЙ ==
c.W_MAIN.mainloop()