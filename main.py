from abc import ABC, abstractmethod
from queue import Queue


# Базовый абстрактный класс для всех животных
class AnimalBase(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def makeNoise(self):
        pass


# Базовый класс для домашних животных
class DomesticAnimal(AnimalBase):
    def __init__(self, name):
        super().__init__(name)


# Базовый класс для диких животных
class WildAnimal(AnimalBase):
    def __init__(self, name):
        super().__init__(name)


# Реализация интерфейса для собаки
class Dog(DomesticAnimal):
    def __init__(self, name):
        super().__init__(name)

    def makeNoise(self):
        print("Гав-гав")


# Реализация интерфейса для кота
class Cat(DomesticAnimal):
    def __init__(self, name):
        super().__init__(name)

    def makeNoise(self):
        print("Мяу-мяу")


# Реализация интерфейса для волка (дикое животное)
class Wolf(WildAnimal):
    def __init__(self, name):
        super().__init__(name)

    def makeNoise(self):
        print("Ууууу")


# Класс для ветеринара
class Vet:
    def treat(self, animal: AnimalBase):
        print(f"Началось лечение животного с кличкой {animal.name}")
        animal.makeNoise()
        print(f"Лечение животного с кличкой {animal.name} закончилось")


# Основной метод программы
if __name__ == "__main__":
    vet = Vet()
    queue = Queue()
    queue.put(Dog("Шарик"))
    queue.put(Cat("Муся"))
    queue.put(Wolf("Серый"))
    queue.put(Dog("Персик"))

    while not queue.empty():
        vet.treat(queue.get())
        print("")
