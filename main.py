from multiprocessing import shared_memory
import tkinter as tk
from tkinter import ttk, Tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def read_and_plot():
    # Считываем данные, обрабатывая исключения
    try:
        data_len = int(len_var.get())
        shift = int(shift_var.get())
    except ValueError:
        tk.messagebox.showerror("Ошибка", "Пожалуйста, введите корректные значения для количества данных и смещения.")
        return
    data_type = data_type_var.get()
    np_data_type = np.int32 if data_type == 'int' else np.float32

    try:
        name = name_var.get()
        shm = shared_memory.SharedMemory(name=name)
    except FileNotFoundError:
        tk.messagebox.showerror("Ошибка", "Не удалось найти именованную разделяемую память с указанным именем.")
        return

    buffer = shm.buf[shift * np_data_type().nbytes:(shift + data_len) * np_data_type().nbytes]
    data = np.frombuffer(buffer, dtype=np_data_type)

    ax.clear()
    ax.plot(data)
    ax.set_title('График считанных данных')
    ax.set_xlabel('Индекс элемента')
    ax.set_ylabel('Значение элемента')
    fig.canvas.draw()


root = Tk()
root.title("Визуализация разделяемой памяти")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Инициализация переменных
name_var = tk.StringVar()
len_var = tk.StringVar()
shift_var = tk.StringVar()
data_type_var = tk.StringVar()

# Элементы интерфейса
name_label = ttk.Label(frame, text="Имя разделяемой памяти:")
name_label.grid(column=0, row=0,
                sticky=(tk.W), padx=5, pady=5)
name_entry = ttk.Entry(frame, textvariable=name_var)
name_entry.grid(column=1, row=0, sticky=(tk.W, tk.E), padx=5, pady=5)

len_label = ttk.Label(frame, text="Количество данных для отображения:")
len_label.grid(column=0, row=1, sticky=(tk.W), padx=5, pady=5)
len_entry = ttk.Entry(frame, textvariable=len_var)
len_entry.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=5, pady=5)

shift_label = ttk.Label(frame, text="Смещение данных для чтения:")
shift_label.grid(column=0, row=2, sticky=(tk.W), padx=5, pady=5)
shift_entry = ttk.Entry(frame, textvariable=shift_var)
shift_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=5, pady=5)

data_type_label = ttk.Label(frame, text="Тип данных одного элемента:")
data_type_label.grid(column=0, row=3, sticky=(tk.W), padx=5, pady=5)
data_type_combobox = ttk.Combobox(frame, textvariable=data_type_var, values=["int", "float"])
data_type_combobox.grid(column=1, row=3, sticky=(tk.W, tk.E), padx=5, pady=5)

# Создание графика
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=10)

# Кнопка для запуска
start_button = ttk.Button(frame, text="Запуск", command=read_and_plot)
start_button.grid(column=0, row=4, columnspan=2, pady=10)

root.mainloop()
