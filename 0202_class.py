class Snow:
    def __init__(self, count: int):
        self.__count = count  # Инкапсуляция

    # Перегрузка оператора сложения
    def __add__(self, n: int):
        return Snow(self.__count + n)

    # Перегрузка оператора вычитания
    def __sub__(self, n: int):
        return Snow(self.__count - n)

    # Перегрузка оператора умножения
    def __mul__(self, n: int):
        return Snow(self.__count * n)

    # Перегрузка оператора деления
    def __truediv__(self, n: int):
        return Snow(self.__count // n)

    # Метод makeSnow
    def makeSnow(self, snowflakes_per_row: int) -> str:
        rows = self.__count // snowflakes_per_row
        remainder = self.__count % snowflakes_per_row
        snowflake_row = "*" * snowflakes_per_row
        result = (snowflake_row + "\n") * rows
        if remainder:
            result += "*" * remainder + "\n"
        return result

    # Перегрузка метода __call__ для вызова объекта как функции
    def __call__(self, n: int):
        self.__count = n

    # Метод для получения количества снежинок
    def get_count(self) -> int:
        return self.__count

    # Метод для установки количества снежинок 
    def set_count(self, count: int):
        if count >= 0:
            self.__count = count
        else:
            raise ValueError("Количество снежинок не может быть отрицательным")

    # Перегрузка метода __str__ для вывода информации о объекте
    def __str__(self):
        return f"Snowflakes: {self.__count}"


# Пример использования
snow = Snow(10)
print(snow)  # Snowflakes: 10

snow = snow + 5
print(snow)  # Snowflakes: 15

snow = snow - 3
print(snow)  # Snowflakes: 12

snow = snow * 2
print(snow)  # Snowflakes: 24

snow = snow / 4
print(snow)  # Snowflakes: 6

print(snow.makeSnow(3))
# ***
# ***

snow(10)  # Вызов объекта как функции
print(snow)  # Snowflakes: 10
