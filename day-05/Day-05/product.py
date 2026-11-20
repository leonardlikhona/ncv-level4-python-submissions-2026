class Product:
    VAT_RATE = 0.15

    def __init__(self, code, name, price):
        self.code = code
        self.name = name

        if price < 0:
            raise ValueError("Price cannot be negative")

        self.price = price

    def __str__(self):
        return f"{self.code} - {self.name}: R{self.price:.2f}"

    def calc_vat(self):
        return self.price * self.VAT_RATE

    def price_including_vat(self):
        return self.price + self.calc_vat()

    def apply_discount(self, percentage):
        discount = self.price * percentage / 100
        return self.price - discount


def main():
    product1 = Product("P001", "Keyboard", 500.00)
    product2 = Product("P002", "Mouse", 300.00)

    print(product1)
    print(product2)

    print("VAT:", f"R{product1.calc_vat():.2f}")
    print("Price including VAT:", f"R{product1.price_including_vat():.2f}")
    print("Price after 10% discount:", f"R{product1.apply_discount(10):.2f}")


main()