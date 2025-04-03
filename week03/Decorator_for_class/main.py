class Product:                                                                         # Объявляем конструктор класса, инициализирующий экземпляр товара.
    def __init__(self, name: str, retail_price: float, purchase_price: float):
        self.name = name                                                               # Присваиваем название товара.
        self.retail_price = retail_price                                               # Присваиваем розничную цену.
        self.purchase_price = purchase_price                                           # Присваиваем закупочную цену.

    @property                                                                          # Декоратор @property делает метод свойством.
    def profit(self) -> float:
        return self.retail_price - self.purchase_price                                 # Возвращаем прибыль.

    @staticmethod                                                                      # Декоратор @staticmethod создает статический метод.
    def average_price(prices: list[float]) -> float:                                   # Вычисляем среднюю цену, обрабатываем случай пустого списка.
        return sum(prices) / len(prices) if prices else 0.0

    @property                                                                          
    def information(self) -> str:                                                      # Добавляем свойство для получения информации о товаре.
        return (f"Product: {self.name}\n"                                              # Возвращаем строку с информацией о товаре.
                f"Retail price: {self.retail_price}\n"
                f"Purchase price: {self.purchase_price}")


product = Product("Jeans", 1200, 800)
print(product.profit)                                                                  # 400
print(Product.average_price([100, 200, 300]))                                          # 200
print(product.information)                                                             # Product: Jeans, Retail price: 1200, Purchase price: 800
