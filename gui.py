import tkinter as tk
from datetime import date
import os
import file_handler
from tkinter.messagebox import askokcancel

class GameNightGui:

    class Drink:

        def _increase(self):
            self.quantity += 1
            self.display_drink.config(text=f"Current Amount of {self.drink_name}: {self.quantity}")
            self.file_handle.data_dict["Drinks"][self.drink_name]["Quantity"] += 1
            self.file_handle.save()

        def _decrease(self):
            self.quantity -= 1
            self.display_drink.config(text=f"Current Amount of {self.drink_name}: {self.quantity}")
            self.file_handle.data_dict["Drinks"][self.drink_name]["Quantity"] -= 1
            self.file_handle.data_dict["Money"] += self.price
            self.file_handle.save()

        def _free_drink(self):
            self.quantity -= 1
            self.display_drink.config(text=f"Current Amount of {self.drink_name}: {self.quantity}")

        def __init__(self, name: str, quantity: int, price: float, frame: tk.Frame, file_handle: file_handler.FileHandler):
            self.file_handle = file_handle
            self.drink_name = name
            self.price = price
            self.quantity = quantity
            self.button_frame = frame
            self.increase_button = tk.Button(self.button_frame, text=f"UP", command=self._increase)
            self.decrease_button = tk.Button(self.button_frame, text=f"DOWN", command=self._decrease)
            self.free_button = tk.Button(self.button_frame, text=f"Free", command=self._free_drink)
            self.display_drink = tk.Label(self.button_frame, text=f"Current Amount of {self.drink_name}: {self.quantity}")

            if not self.drink_name in self.file_handle.data_dict["Drinks"]:
                self.file_handle.data_dict["Drinks"][self.drink_name] = {"Quantity": self.quantity, "Price": self.price}


    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1000x1000")
        self.file_handle = file_handler.FileHandler()

        self.label = tk.Label(self.root, text="Game Night Drinks", font=('Arial', 18))
        self.label.grid(row=0, padx=10, pady=10)
        self.current_row_iter = 0

        self.button_frame = tk.Frame(self.root)
        self.current_drinks = list()
        self.current_labels = list()

        self.initialize_drinks()

        self.enter_drink = tk.Label(self.button_frame, text="Enter New Drink:")
        self.enter_drink.grid(sticky='SW', column=0, row=100)
        self.new_drink_field = tk.Entry(self.button_frame, width=10)
        self.new_drink_field.insert(0, "Drink Name")
        self.new_drink_field.grid(sticky="SW", column=1, row=100)
        self.add_price_field = tk.Entry(self.button_frame, width=10)
        self.add_price_field.insert(0, "Price")
        self.add_price_field.grid(sticky="SW", column=2, row=100)
        self.add_drink_button = tk.Button(self.button_frame, text="Add Drink", command=self.add_drink)
        self.add_drink_button.grid(sticky="SE", column=3, row=100)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def initialize_drinks(self):
        self.file_handle.load()
        for drink in self.file_handle.data_dict["Drinks"]:
            self.current_labels.append(tk.Label(self.button_frame, text=f"{drink}:"))
            self.current_labels[len(self.current_labels) - 1].grid(row=len(self.current_labels) - 1, column=0)
            self.current_drinks.append(self.Drink(f"{drink}", self.file_handle.data_dict["Drinks"][drink]["Quantity"],
                                       self.file_handle.data_dict["Drinks"][drink]["Price"], self.button_frame, self.file_handle))
            self.current_drinks[len(self.current_drinks) - 1].increase_button.grid(row=len(self.current_drinks) - 1, column=1)
            self.current_drinks[len(self.current_drinks) - 1].decrease_button.grid(row=len(self.current_drinks) - 1, column=2)
            self.current_drinks[len(self.current_drinks) - 1].free_button.grid(row=len(self.current_drinks) - 1, column=3)
            self.current_drinks[len(self.current_drinks) - 1].display_drink.grid(row=len(self.current_drinks) - 1, column=4)
        self.button_frame.grid(sticky='W')

    def add_drink(self):
        self.current_drinks.append(self.Drink(self.new_drink_field.get(), 0, float(self.add_price_field.get().replace(",", ".")), self.button_frame, self.file_handle))

        self.current_labels.append(tk.Label(self.button_frame, text=self.current_drinks[-1].drink_name))
        self.current_labels[len(self.current_labels)-1].grid(row=len(self.current_labels) - 1, column=0)
        self.current_drinks[len(self.current_drinks) - 1].increase_button.grid(row=len(self.current_drinks) - 1, column=1)
        self.current_drinks[len(self.current_drinks) - 1].decrease_button.grid(row=len(self.current_drinks) - 1, column=2)
        self.current_drinks[len(self.current_drinks) - 1].display_drink.grid(row=len(self.current_drinks) - 1, column=3)
        print(self.new_drink_field.get())

    def gen_buttons(self, number_of_buttons:int):
        for i in range(number_of_buttons):
            self.current_labels.append(tk.Label(self.button_frame, text=f"Drink {i}:"))
            self.current_labels[len(self.current_labels) - 1].grid(row=len(self.current_labels) - 1, column=0)
            self.current_drinks.append(self.Drink(f"Drink {i}", 0, 0, self.button_frame, self.file_handle))
            self.current_drinks[len(self.current_drinks) - 1].increase_button.grid(row=len(self.current_drinks) - 1, column=1)
            self.current_drinks[len(self.current_drinks) - 1].decrease_button.grid(row=len(self.current_drinks) - 1, column=2)
            self.current_drinks[len(self.current_drinks) - 1].display_drink.grid(row=len(self.current_drinks) - 1, column=3)
        self.button_frame.grid(sticky='W')

    def on_closing(self):
        if askokcancel("Quit", "Do you want to quit?"):
            self.file_handle.save(auto_save=False)
            self.root.destroy()


def hello_world():
    print("Hello World!")
