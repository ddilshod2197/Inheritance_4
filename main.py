# 4. Restoran buyurtmalari
class Order:
    def __init__(self, name, price, service_fee_percent=10):
        self.name = name
        self.price = price                   
        self.service_fee = service_fee_percent

    def total_cost(self):
        """Taom narxi + xizmat haqi"""
        return self.price * (1 + self.service_fee / 100)

    def __str__(self):
        total = self.total_cost()
        return f"{self.name:12} | {self.price:6.2f}$ | {self.service_fee:4}% | {total:8.2f}$"


class MainDish(Order):
    def __str__(self):
        total = self.total_cost()
        return f"🍕 {self.name:10} → {self.price:5.2f}$ + {self.service_fee}% → {total:5.2f}$"


class SideDish(Order):
    def __str__(self):
        total = self.total_cost()
        return f"🥗 {self.name:10} → {self.price:5.2f}$ + {self.service_fee}% → {total:5.2f}$"


def show_order_summary(orders):
    print("\n" + "═" * 60)
    print("  RESTAURAN BUYURTMASI  ".center(60))
    print("═" * 60)
    print("Taom nomi      | Narx    | Xizmat % | Jami narx")
    print("─" * 60)

    subtotal = 0
    service_total = 0

    for item in orders:
        print(item)
        cost = item.total_cost()
        subtotal += item.price
        service_total += (cost - item.price)

    grand_total = subtotal + service_total

    print("─" * 60)
    print(f"Subtotal (taomlar):                  {subtotal:10.2f}$")
    print(f"Xizmat haqi jami:                     {service_total:10.2f}$")
    print(f"Umumiy to‘lov:                        {grand_total:10.2f}$")
    print("═" * 60 + "\n")


orders = [
    MainDish("Pizza Margherita", 15.00, 10),
    MainDish("Pasta Carbonara", 18.50, 12),
    SideDish("Sezar salat", 7.00, 10),
    SideDish("Qovurilgan kartoshka", 4.50, 10),
    MainDish("Steyk", 28.00, 15),
]

show_order_summary(orders)


print("\nSizning misol buyurtmangiz:\n")
example_orders = [
    MainDish("Pizza", 15, 10),
    SideDish("Salat", 5, 10),
]

show_order_summary(example_orders)
