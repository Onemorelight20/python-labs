class Animal:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"name: {self.name}"


class Mammal(Animal):
    def __init__(self, name: str, weight_in_kilos: float):
        super().__init__(name)
        self.weight_in_kilos = weight_in_kilos

    def __str__(self) -> str:
        return super().__str__() + f" weight in kilos: {self.weight_in_kilos}"


class Bird(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.color = color

    def __str__(self) -> str:
        return super().__str__() + f" color: {self.color}"


class Insect(Animal):
    def __init__(self, name: str, num_of_eyes: int):
        super().__init__(name)
        self.num_of_eyes = num_of_eyes

    def __str__(self) -> str:
        return super().__str__() + f" number of eyes: {self.num_of_eyes}"


class Reptile(Animal):
    def __init__(self, name: str, specie: str):
        super().__init__(name)
        self.specie = specie

    def __str__(self) -> str:
        return super().__str__() + f" specie: {self.specie}"


class Fish(Animal):
    def __init__(self, name: str, length_in_meters: float):
        super().__init__(name)
        self.length_in_meters = length_in_meters

    def __str__(self) -> str:
        return super().__str__() + f" length in meters: {self.length_in_meters}"