# Римское число

Создайте свой класс Roman (РимскоеЧисло), представляющий римское число и подддерживающий операции +,-,*,/.


```PYTHON
class Roman:                                                                     # Класс для работы с римскими числами.
    
    ARABIC_MIN = 1                                                               # Минимальное допустимое арабское число.
    ARABIC_MAX = 3999                                                            # Максимальное допустимое арабское число.
    ROMAN_MIN = "I"                                                              # Минимальное римское число.
    ROMAN_MAX = "MMMCMXCIX"                                                      # Максимальное римское число.

    LETTERS = ["M", "CM", "D", "CD", "C", "XC", "L",                             # Kонвертация между системами счисления.
               "XL", "X", "IX", "V", "IV", "I"]
    NUMBERS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    def __init__(self, value):                                                   # Инициализирует объект Roman из арабского или римского числа.
        if not isinstance(value, (int, str)):                                    # value: int (арабское число) или str (римское число).
            raise TypeError("Нельзя создать римское число из {0}".
                            format(type(value)))

        if isinstance(value, int):
            self.__check_arabic(value)                                           # Проверка диапазона.
            self._arabic = value                                                 # Сохранение арабского числа.
        elif isinstance(value, str):
            self._arabic = self.to_arabic(value)                                 # Конвертация из римского числа.

    def __add__(self, other):

        if isinstance(other, Roman):                                             # Сложение с другим римским или другим целым числом.                 
            return Roman(self._arabic + other.arabic)                            
        elif isinstance(other, int):
            return Roman(self._arabic + other)
        else:
            raise TypeError("Нельзя сложить римское число с {0}".
                            format(type(other)))

    def __sub__(self, other):                                                    # Вычитание другого римского или другого целого числа.
        if isinstance(other, Roman):
            return Roman(self._arabic - other.arabic)
        elif isinstance(other, int):
            return Roman(self._arabic - other)
        else:
            raise TypeError("Нельзя отнять от римского числа {0}".
                            format(type(other)))

    def __mul__(self, other):                                                    # Умножение на другое римского или другого целого числа.
        if isinstance(other, Roman):
            return Roman(self._arabic * other.arabic)
        elif isinstance(other, int):
            return Roman(self._arabic * other)
        else:
            raise TypeError("Нельзя умножить римское число на {0}".
                            format(type(other)))

    def __floordiv__(self, other):                                               # Целочисленное деление на другой римское или другое целое число.
        if isinstance(other, Roman):
            return Roman(self._arabic // other.arabic)
        elif isinstance(other, int):
            return Roman(self._arabic // other)
        else:
            raise TypeError("Нельзя поделить римское число на {0}".
                            format(type(other)))

    def __truediv__(self, other):                                                # Деление, при котором любое деление для римского числа считается делением нацело
        return self.__floordiv__(other)

    def __str__(self):                                                           # Строковое представление - римское число.
        return Roman.to_roman(self._arabic)

    @staticmethod
    def __check_arabic(value):                                                   # Проверяет, что арабское число в допустимом диапазоне.
        if value >= 1 and value <= 3999:
            return True
        else:
            raise ValueError(f"{value} не входит в интервал [1-3999]")

    @staticmethod
    def __check_roman(value):                                                    # Проверяет корректность римского числа.
        for ch in value:
            if ch not in Roman.LETTERS:
                raise ValueError(f"{ch} является недопустимым символом.")
        return True

    @property
    def arabic(self):                                                            # Возвращает арабское представление числа.
        return self._arabic

    @staticmethod
    def to_arabic(roman):                                                        # Конвертирует римское число в арабское.
        def letter_to_number(letter):
            letter = str.upper(letter)
            if letter == "I":
                return 1
            elif letter == "V":
                return 5
            elif letter == "X":
                return 10
            elif letter == "L":
                return 50
            elif letter == "C":
                return 100
            elif letter == "D":
                return 500
            else:
                return 1000

        Roman.__check_roman(roman)

        i = 0                                                                   # Позиция в строке roman
        value = 0                                                               # Преобразованное число

        while i < len(roman):

            number = letter_to_number(roman[i])

            i += 1

            if i == len(roman):                                                 # В строке roman больше не осталось символов, добавляем number.
                value += number
            else:                                                               
                next_number = letter_to_number(roman[i])                        
                if next_number > number:                                        # Комбинируем цифры и перемещаем i к следующей.
                    value += next_number - number
                    i += 1
                else:                                                           # Добавляем следующую цифру.
                    value += number

        Roman.__check_arabic(value)
        return value

    @staticmethod
    def to_roman(arabic):                                                       # Конвертирует арабское число в римское.
        Roman.__check_arabic(arabic)

        roman = ""
        n = arabic                                                              # n - часть arabic, которую осталось преобразовать

        for i, number in enumerate(Roman.NUMBERS):
            while n >= number:
                roman += Roman.LETTERS[i]
                n -= Roman.NUMBERS[i]

        return roman
```
