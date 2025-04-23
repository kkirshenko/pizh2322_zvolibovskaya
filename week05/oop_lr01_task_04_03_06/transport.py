from abc import ABC, abstractmethod  # Импортируем ABC (Abstract Base Class) и abstractmethod из модуля abc

class Transport(ABC):
    # Абстрактный базовый класс для представления транспорта
    def __init__(self, speed: float, capacity: int) -> None:
        self.speed: float = speed  # Инициализируем атрибут speed (скорость)
        self.capacity: int = capacity  # Инициализируем атрибут capacity (вместимость)

    @abstractmethod
    def move(self) -> None:
        # Метод для движения транспорта (должен быть реализован в подклассах)
        pass  # Абстрактный метод move, который должен быть реализован в подклассах

    def stop(self) -> None:
        # Метод для остановки транспорта
        print(f"{self.__class__.__name__}: Остановился.")  # Выводим сообщение об остановке транспорта (название класса)

    def __str__(self) -> str:
        # Метод для строкового представления транспорта
        return (f"{self.__class__.__name__}:"  # Возвращаем строку с информацией о транспорте (название класса)
                f"скорость={self.speed}, вместимость={self.capacity}")  # Добавляем информацию о скорости и вместимости

class WaterTransport(Transport):
    # Класс для представления водного транспорта
    def __init__(self, speed: float, capacity: int, water_type: str) -> None:
        # Инициализация водного транспорта с указанием скорости, вместимости и типа воды
        super().__init__(speed, capacity)  # Вызываем конструктор базового класса Transport
        self.water_type: str = water_type  # Инициализируем атрибут water_type (тип воды)

    def move(self) -> None:
        # Реализация метода движения для водного транспорта
        print(f"{self.__class__.__name__}: Плывет со скоростью"  # Выводим сообщение о движении водного транспорта (название класса)
              f"{self.speed} узлов по {self.water_type}.")  # Добавляем информацию о скорости и типе воды

class WheeledTransport(Transport):
    # Класс для представления колесного транспорта
    def __init__(self, speed: float, capacity: int, wheels: int) -> None:
        # Инициализация колесного транспорта с указанием скорости, вместимости и количества колес
        super().__init__(speed, capacity)  # Вызываем конструктор базового класса Transport
        self.wheels: int = wheels  # Инициализируем атрибут wheels (количество колес)

    def move(self) -> None:
        # Реализация метода движения для колесного транспорта
        print(f"{self.__class__.__name__}: Едет со скоростью"  # Выводим сообщение о движении колесного транспорта (название класса)
              f"{self.speed} км/ч на {self.wheels} колесах.")  # Добавляем информацию о скорости и количестве колес

class Car(WheeledTransport):
    # Класс для представления автомобиля
    def __init__(self, speed: float, capacity: int, fuel_type: str) -> None:
        # Инициализация автомобиля с указанием скорости, вместимости и типа топлива
        super().__init__(speed, capacity, wheels=4)  # Вызываем конструктор базового класса WheeledTransport, устанавливая количество колес равным 4
        self.fuel_type: str = fuel_type  # Инициализируем атрибут fuel_type (тип топлива)

    def move(self) -> None:
        # Реализация метода движения для автомобиля
        print(f"{self.__class__.__name__}: Едет на {self.fuel_type} "  # Выводим сообщение о движении автомобиля (название класса)
              f"со скоростью {self.speed} км/ч.")  # Добавляем информацию о типе топлива и скорости

    def honk(self) -> None:
        # Метод для подачи звукового сигнала автомобилем
        print("Автомобиль: Бип-бип!")  # Выводим звук автомобиля