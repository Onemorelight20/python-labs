from animals import *


def main():
    mammal = Mammal("Oleh", 10)
    bird = Bird("Golden bird", "yellow")
    insect = Insect("Dan", 4)
    reptile = Reptile("Jakob", "crocodile")
    fish = Fish("Maria", 3)

    print("Created objects:")
    print(mammal)
    print(bird)
    print(insect)
    print(reptile)
    print(fish)


if __name__ == '__main__':
    main()
