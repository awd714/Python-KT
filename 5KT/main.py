from tkinter import Tk, Label
from datetime import date


def main():
    today = date.today()

    window = Tk()
    window.title('Задачи')
    window.geometry('650x450')
    window.configure(bg='black')

    title = Label(
        window,
        text='Мои текущие задачи',
        font=('Times New Roman', 30, 'bold', 'underline'),
        fg='yellow',
        bg='black'
    )
    title.pack(pady=20)

    file = open('tasks.txt', 'r', encoding='utf-8')

    for line in file:
        task = line.strip()

        if task:
            task_date, task_name = task.split('|')
            task_date = date.fromisoformat(task_date)

            days = (task_date - today).days

            if days < 0:
                message = f'Прошло {abs(days)} дней от {task_name}'
                color = 'red'

            elif days == 0:
                message = f'Прямо сейчас происходит {task_name}'
                color = 'orange'

            else:
                message = f'Осталось {days} дней до {task_name}'
                color = 'lightblue'

            label = Label(
                window,
                text=message,
                font=('Arial', 14),
                fg=color,
                bg='black'
            )
            label.pack(anchor='w', padx=100)

    file.close()

    window.mainloop()


main()
