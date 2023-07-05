import tkinter
import tkinter as tk


class GameNightGui:


    class Drink:

        def _increase(self):
            self.quantity += 1
            self.display_drink.config(text=f"Current Ammount of {self.drink_name}: {self.quantity}")
            print(self.quantity)

        def _decrease(self):
            self.quantity -= 1
            self.display_drink.config(text=f"Current Ammount of {self.drink_name}: {self.quantity}")
            print(self.quantity)

        def __init__(self, name: str, quantity: int, price: float, frame: tk.Frame):
            self.drink_name = name
            self.price = price
            self.quantity = quantity

            self.button_frame = frame
            self.increase_button = tk.Button(self.button_frame, text=f"UP", command=self._increase)
            self.decrease_button = tk.Button(self.button_frame, text=f"down", command=self._decrease)
            self.display_drink = tk.Label(self.button_frame, text=f"Current Ammount of {self.drink_name}: {self.quantity}")

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.label = tk.Label(self.root, text="Game Night Drinks", font=('Arial', 18))
        self.label.grid(row=0, padx=10, pady=10)

        self.button_frame = tk.Frame(self.root)
        self.current_drinks = list()


        self.gen_buttons(10)
        self.gen_label(10)


        self.enter_drink = tk.Label(self.button_frame, text="Enter New Drink:")
        self.enter_drink.grid(sticky='SW',column=0, row=100)
        self.new_drink_field = tk.Entry(self.button_frame, width=10)
        self.new_drink_field.insert(0, "Drink Name")
        self.new_drink_field.grid(sticky="SW", column=1, row=100)
        self.add_price_field = tk.Entry(self.button_frame, width=10)
        self.add_price_field.insert(0, "Price")
        self.add_price_field.grid(sticky="SW", column=2, row=100)
        self.add_drink_button = tk.Button(self.button_frame, text="Add Drink", command=self.add_drink)
        self.add_drink_button.grid(sticky="SE", column=3, row=100)

        self.root.mainloop()

    def add_drink(self):
        self.current_drinks.append(self.Drink(self.new_drink_field.get(), 0, self.add_price_field.get(), self.button_frame))

        print(self.new_drink_field.get())

    def gen_buttons(self, number_of_buttons:int):
        for i in range(number_of_buttons):
            self.current_drinks.append(self.Drink(f"Drink {i}", 0, 0, self.button_frame))
            self.current_drinks[i].increase_button.grid(row=i, column=1)
            self.current_drinks[i].decrease_button.grid(row=i, column=2)
            self.current_drinks[i].display_drink.grid(row=i, column=3)
        self.button_frame.grid(sticky='W')

    def gen_label(self, number_of_buttons:int):
        self.current_labels = list()
        for i in range(number_of_buttons):
            self.current_labels.append(tk.Label(self.button_frame, text=f"Drink {i}:"))
            self.current_labels[i].grid(row=i, column=0)
        self.button_frame.grid(sticky='W')

def hello_world():
    print("Hello World!")