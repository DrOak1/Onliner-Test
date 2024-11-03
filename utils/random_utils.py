import random


class RandomUtils:
    @staticmethod
    def get_random_value():
        rand_val = random.sample(range(1, 11), 2)
        return sorted(rand_val)