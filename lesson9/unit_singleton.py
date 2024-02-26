import unittest

class Alex(Engineer):
    _instance = None  # Приватное статическое поле для хранения единственного экземпляра класса

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, name, age):
        super().__init__(name, age)


class TestSingleton(unittest.TestCase):
    def test_singleton_instance(self):
        alex1 = Alex("Alex", 25)
        alex2 = Alex("Alex", 25)
        self.assertIs(alex1, alex2)  # Проверяем, что оба объекта являются одним и тем же экземпляром


if __name__ == "__main__":
    unittest.main()
