


class Microwave:
    def __init__(self, brand:str, power_rating:str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on:bool = False

    def turn_on(self):
        if self.turned_on:
            print(F"Microwave {self.brand} is already turn on")
        else:
            self.turned_on = True
            print(f"Microwave {self.brand} is turned on")

    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"Microwave {self.brand} is now turned on")
        else:
            print(f"Microwave {self.brand} is already turned off")

    def run(self, seconds:int)->None:
        if self.turned_on:
            print(f"Running ({self.brand} for {seconds} seconds)")
        else:
            print(f"A mystical force whispers: 'Turn on your microwave first'")

    def __add__(self, other):
        return f"{self.brand} + {other.brand}"

    def __str__(self):
        return f"{self.brand} (Rating: {self.power_rating})"

# smeg: Microwave = Microwave()
smeg:Microwave = Microwave(brand="Iowa", power_rating='B')
bosch:Microwave = Microwave(brand="Clear", power_rating='C')
print(smeg + bosch)
print(smeg)

