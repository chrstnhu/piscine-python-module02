import time
from random import randint
import os

def log(func):
    '''
    Decorator that logs the function and the time it takes
    '''
    f = open("machine.log", "w")
    def wrapper(*args, **kwargs):
        f = open("machine.log", "a")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        elapsed_time = (end_time - start_time) * 1000

        # Replace '_' to ' ', capitalize the 1st letter, ajust lenght to 20 characters
        name = func.__name__.replace('_', ' ').title().capitalize().ljust(20)

        f.write(f"(chrhu)Running: {name} ")
        f.write(f"[ exec-time = {elapsed_time:.3f} ms ]\n")

        f.close()
        return result
    return wrapper


class CoffeeMachine():
    water_level = 100
    
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)