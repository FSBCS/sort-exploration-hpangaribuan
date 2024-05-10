import random

class RandomList:
    def __init__(self):
        raise NotImplementedError("This class cannot be instantiated")

    @classmethod
    def generate_list(cls, n, min_val=-100, max_val=100):
        return [random.randint(min_val, max_val) for _ in range(n)]