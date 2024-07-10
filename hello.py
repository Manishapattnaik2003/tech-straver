import tkinter as tk
from tkinter import ttk, messagebox

def inches_to_feet(inches):
    return inches / 12

def feet_to_inches(feet):
    return feet * 12

def inches_to_yards(inches):
    return inches / 36

def yards_to_inches(yards):
    return yards * 36

def feet_to_yards(feet):
    return feet / 3

def yards_to_feet(yards):
    return yards * 3

def inches_to_millimeters(inches):
    return inches * 25.4

def millimeters_to_inches(mm):
    return mm / 25.4

def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def miles_to_kilometers(miles):
    return miles * 1.60934

def kilometers_to_miles(km):
    return km / 1.60934

def convert(value, from_unit, to_unit):
    conversions = {
        'inches': {
            'feet': inches_to_feet,
            'yards': inches_to_yards,
            'millimeters': inches_to_millimeters
        },
        'feet': {
            'inches': feet_to_inches,
            'yards': feet_to_yards,
            'meters': feet_to_meters
        },
        'yards': {
            'inches': yards_to_inches,
            'feet': yards_to_feet
        },
        'miles': {
            'kilometers': miles_to_kilometers
        },
        'millimeters': {
            'inches': millimeters_to_inches
        },
        'meters': {
            'feet': meters_to_feet
        },
        'kilometers': {
            'miles': kilometers_to_miles
        }
    }

    if from_unit in conversions and to_unit in conversions[from_unit]:
        return conversions[from_unit][to_unit](value)
    else:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported")

class MeasurementConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Measurement Converter")

        self.value_label = ttk.Label(root, text="Value:")
        self.value_label.grid(column=0, row=0, padx=10, pady=10)

        self.value_entry = ttk.Entry(root)
        self.value_entry.grid(column=1, row=0, padx=10, pady=10)

        self.from_unit_label = ttk.Label(root, text="From Unit:")
        self.from_unit_label.grid(column=0, row=1, padx=10, pady=10)

        self.from_unit_combobox = ttk.Combobox(root, values=[
            'inches', 'feet', 'yards', 'miles', 'millimeters', 'meters', 'kilometers'
        ])
        self.from_unit_combobox.grid(column=1, row=1, padx=10, pady=10)

        self.to_unit_label = ttk.Label(root, text="To Unit:")
        self.to_unit_label.grid(column=0, row=2, padx=10, pady=10)

        self.to_unit_combobox = ttk.Combobox(root, values=[
            'inches', 'feet', 'yards', 'miles', 'millimeters', 'meters', 'kilometers'
        ])
        self.to_unit_combobox.grid(column=1, row=2, padx=10, pady=10)

        self.convert_button = ttk.Button(root, text="Convert", command=self.convert)
        self.convert_button.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(root, text="Result:")
        self.result_label.grid(column=0, row=4, padx=10, pady=10)

        self.result_value_label = ttk.Label(root, text="")
        self.result_value_label.grid(column=1, row=4, padx=10, pady=10)

    def convert(self):
        try:
            value = float(self.value_entry.get())
            from_unit = self.from_unit_combobox.get()
            to_unit = self.to_unit_combobox.get()

            if not from_unit or not to_unit:
                raise ValueError("Please select both units for conversion.")

            result = convert(value, from_unit, to_unit)
            self.result_value_label.config(text=f"{result:.4f}")
        except ValueError as e:
            messagebox.showerror("Conversion Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MeasurementConverterApp(root)
    root.mainloop()
