people = ["Катя", "Настя", "Маша", "Даша"]

def say_to_all(action, names):                                     # Функция, которая применяет переданное действие ко всем именам.
    for name in names:
        print(action(name))

say_to_all(lambda name: f'Привет, {name}!', people)                # Первый вызов - печатаем приветствия.
say_to_all(lambda name: f'До завтра, {name}!', people)             # Второй вызов - печатаем прощания.