from abc import ABC, abstractmethod
class Abst(ABC):
    @abstractmethod
    def momo1(self):
        pass

    @abstractmethod
    def momo2(self):
        pass

class Home(Abst):
    def momo1(self):
        print('Go home')

    def momo2(self):
        print('Go home 2')

    @staticmethod
    def static_method():
        print('Статический метод')


a = Home
a().momo1()
a().momo2()
Home().static_method()
