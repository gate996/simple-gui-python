import tkinter as tk

def button_click():
    label.config(text="Привет, мир!")

# Создаем объект окна
window = tk.Tk()
window.title("Простое GUI-приложение")

# Создаем метку
label = tk.Label(window, text="Нажмите кнопку", font=("Arial", 14))
label.pack(pady=20)

# Создаем кнопку
button = tk.Button(window, text="Нажми меня", font=("Arial", 12), padx=10, pady=5, command=button_click)
button.pack()

# Запускаем главный цикл окна
window.mainloop()
