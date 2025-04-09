from abc import ABC, abstractmethod                                    # Инструменты для работы с абстрактными классами.

class Pizza(ABC):                                                      # Определяет общий интерфейс для всех пицц
    def __init__(self, name: str, dough: str, sauce: str, toppings: list, price: float):
        self.name = name                                               # Название пиццы
        self.dough = dough                                             # Тип теста
        self.sauce = sauce                                             # Тип соуса
        self.toppings = toppings                                       # Список начинок
        self.price = price                                             # Цена пиццы
    
    def prepare(self):                                                 # Процесс подготовки пиццы
        print(f"=== Готовим {self.name} ===")
        print(f"Замешиваем {self.dough} тесто...")
        print(f"Добавляем {self.sauce} соус...")
        print("Добавляем начинку:")
        for topping in self.toppings:
            print(f"- {topping}")
    
    def bake(self):                                                    # Процесс выпекания
        print("Выпекаем 30 минут при 200°C")
    
    def cut(self):                                                     # Процесс нарезки
        print("Нарезаем на 8 кусочков")
    
    def box(self):                                                     # Процесс упаковки
        print("Упаковываем в фирменную коробку")
    
    def __str__(self):                                                 # Строковое представление
        return f"{self.name} ({self.price} руб.)"
    
class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__(
            name="Пепперони",
            dough="тонкое",
            sauce="томатный",
            toppings=["пепперони", "сыр моцарелла"],
            price=789
        )

class BBQPizza(Pizza):
    def __init__(self):
        super().__init__(
            name="Барбекю",
            dough="толстое",
            sauce="барбекю",
            toppings=["курица", "бекон", "лук", "сыр моцарелла"],
            price=1009
        )

class SeafoodPizza(Pizza):
    def __init__(self):
        super().__init__(
            name="Дары Моря",
            dough="тонкое",
            sauce="чесночный",
            toppings=["креветки", "мидии", "лук", "сыр моцарелла"],
            price=1280
        )
class Order:                                                          # Хранит список пицц как объекты
    order_counter = 0                                                 # Счетчик заказов
    
    def __init__(self):
        Order.order_counter += 1
        self.order_number = Order.order_counter                       # Номер текущего заказа
        self.pizzas = []                                              # Список пицц в заказе
    
    def add(self, pizza: Pizza):                                      # Добавление пиццы в заказ
        self.pizzas.append(pizza)
    
    def total(self) -> float:                                         # Подсчет общей суммы
        return sum(pizza.price for pizza in self.pizzas)
    
    def execute(self):                                                # Выполнение заказа
        print(f"\n=== Начинаем готовить заказ №{self.order_number} ===")
        for pizza in self.pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()
        print(f"=== Заказ №{self.order_number} готов! ===")
    
    def __str__(self):                                                # Строковое представление заказа
        if not self.pizzas:
            return "Заказ пуст"
        order_list = "\n".join(str(pizza) for pizza in self.pizzas)
        return f"Заказ №{self.order_number}:\n{order_list}\nИтого: {self.total()} руб."
    
class Terminal:                                                       # Управляет состоянием текущего заказа, oбрабатывает взаимодействие с пользователем, создает меню
    def __init__(self):
        self.menu = {                                                 # Меню пиццерии
            1: PepperoniPizza(),
            2: BBQPizza(),
            3: SeafoodPizza()
        }
        self.current_order = None                                     # Текущий заказ
        self.show_menu = True                                         # Флаг отображения меню
    
    def display_menu(self):                                           # Отображение меню
        print("\n=== Меню пиццерии ===")
        for num, pizza in self.menu.items():
            print(f"{num}. {pizza}")
        print("4. Завершить заказ")
        print("5. Отменить заказ")
    
    def process_command(self, menu_item: int):                        # Обработка команд
        if menu_item == 4 and self.current_order and self.current_order.pizzas:
            self.confirm_order()                                      # Подтверждение заказа
        elif menu_item == 5:
            self.cancel_order()                                       # Отмена заказа
        elif menu_item in self.menu:
            if not self.current_order:
                self.current_order = Order()                          # Создание нового заказа
            pizza = self.menu[menu_item]
            self.current_order.add(pizza)                             # Добавление пиццы
            print(f"Добавлено: {pizza.name}")
        else:
            print("Неверный пункт меню!")
    
    def confirm_order(self):                                          # Подтверждение заказа
        print("\n=== Ваш заказ ===")
        print(self.current_order)
        
        while True:
            try:
                payment = float(input("Введите сумму для оплаты: "))
                if payment < self.current_order.total():
                    print("Недостаточно средств!")
                    continue
                
                self.accept_payment(payment)                          # Прием оплаты
                self.current_order.execute()                          # Выполнение заказа
                self.current_order = None                             # Сброс текущего заказа
                break
            except ValueError:
                print("Пожалуйста, введите число!")
    
    def cancel_order(self):                                           # Отмена заказа
        if self.current_order:
            print(f"\nЗаказ №{self.current_order.order_number} отменен")
            self.current_order = None
        else:
            print("Нет активного заказа для отмены")
    
    def accept_payment(self, amount: float):                          # Прием платежа
        change = amount - self.current_order.total()
        print(f"Принято {amount} руб.")
        if change > 0:
            print(f"Сдача: {change} руб.")
        print("Оплата прошла успешно!")
    
    def run(self):                                                    # Основной цикл работы терминала
        print("=== Добро пожаловать в пиццерию! ===")
        
        while True:
            if self.show_menu:
                self.display_menu()
            
            try:
                command = int(input("\nВыберите пункт меню: "))
                self.process_command(command)
                
                if not self.current_order:
                    another = input("Хотите сделать еще один заказ? (да/нет): ").lower()
                    if another != 'да':
                        print("До свидания! Приходите еще!")
                        break
                    self.show_menu = True
                else:
                    self.show_menu = False
            except ValueError:
                print("Пожалуйста, введите номер пункта меню!")
if __name__ == "__main__":                                           # Создание одного терминала, который управляет всем процессом
    terminal = Terminal()                                            # Создание терминала
    terminal.run()                                                   # Запуск основного цикла
