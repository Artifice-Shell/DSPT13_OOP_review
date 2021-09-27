import random
import time


class Product:

    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        random_id = self._rollD9999999()
        self.identifier = random_id

    def _rollD9999999(self):
        """An internal method which simulates rolling a 20-sided die."""

        print(f'Determining stats for {self.name}...')
        time.sleep(1)
        print('Rolling 20-sided dice...')
        time.sleep(2)

        die_number = random.randint(1000000, 9999999)
        print(f'Rolled a {die_number}!')

        return die_number
