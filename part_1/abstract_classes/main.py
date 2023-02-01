
# Создайте абстрактный класс автомобиля Transport c абстрактными методами
# - start_engine
# - stop_engine
# - move
# - stop

# Унаследуйте от него три класса Boat, Car, Electroscooter
# для каждого из требуемых методов через print укажите какое-либо действие.
# К примеру start_engine -> print('Двигатель катера запущен')

# Создайте класс Person у которого будет один единственный метод use_transport.
# В данный метод в качестве параметра должен передаваться объект реализующий интерфейс Transport
# Метод для этого объекта должен запускать двигатель, двигаться куда-то, тормозить и глушить двигатель.
# Для текстовой анимации Вы можете использовать любые фразы, или воспользоваться нашей подборкой:
# Boat:
#    - Катер громко затарахтел
#    - Двигатель катера чихнул напоследок и заглох
#    - Катер быстро набирает скорость
#    - Катер остановился
# Car:
#    - Машина заурчала двигателем
#    - Машина стоит с заглушенным двигателем
#    - Машина едет к цели назначения
#    - Машина остановилась
# Electroscooter:
#    - Мигнул светодиодом
#    - Мигнул светодиодом дважды
#    - Прохожие в ужасе разбегаются от очередного камикадзе
#    - Торможение об стену прошло успешно


# Корректным решением будет когда экземпляр класса Person смог использовать все три различных транспорта

# в решении класс Transport должен быть унаследован от ABC
# все методы Transport должны быть помечены декоратором @abstractmethod
# Классы Boat, Car, Electroscooter должны быть унаследованы от Transport

# экземпляр класса Person должен поочередно взаимодействовать с объектами Car, Boat, Electroscooter

# код должен выполняться не выбрасывая исключений

from abc import ABC, abstractmethod


class Transport(ABC):
    """
    The Transport class inherits from the ABC class of the abc library and is the base abstract class
    defining abstract methods (start_engine(), stop_engine(), move(), stop(self))
    which should be overridden in child classes.
    """
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Boat(Transport):
    """
    The Boat class inherits from the base abstract class Transport . The abstract methods of the base
    class(start_engine(), stop_engine(), move(), stop(self)) are redefined in the class in relation
    to the characteristics of the type of vehicle.
    """
    def start_engine(self):
        print("Катер громко затарахтел")

    def stop_engine(self):
        print("Двигатель катера чихнул напоследок и заглох")

    def move(self):
        print("Катер, рассекая волны, быстро набирает скорость")

    def stop(self):
        print("Катер остановился")

class Car(Transport):
    """
    The Car class inherits from the base abstract class Transport . The abstract methods of the base
    class(start_engine(), stop_engine(), move(), stop(self)) are redefined in the class in relation
    to the characteristics of the type of vehicle.
    """
    def start_engine(self):
        print("Машина заурчала двигателем")

    def stop_engine(self):
        print("Машина стоит с заглушенным двигателем")

    def move(self):
        print("Машина едет к цели назначения")

    def stop(self):
        print("Машина остановилась")

class Electroscooter(Transport):
    """
    The Electroscooter class inherits from the base abstract class Transport . The abstract methods of the base
    class(start_engine(), stop_engine(), move(), stop(self)) are redefined in the class in relation
    to the characteristics of the type of vehicle.
    """
    def start_engine(self):
        print("Мигнул светодиодом")

    def stop_engine(self):
        print("На последок мигнул светодиодом дважды")

    def move(self):
        print("Прохожие в ужасе разбегаются от очередного камикадзе")

    def stop(self):
        print("Торможение об стену прошло успешно")


class Person:
    """
    The Person class has a single use_transport method.
    An object implementing the Transport interface is passed to this method as a parameter
    The method for this object starts the engine, moves somewhere, brakes and turns off the engine.
    """
    def use_transport(self, transport):
        transport.start_engine()
        transport.move()
        transport.stop()
        transport.stop_engine()


# Отрезок кода для самопроверки.
# Запустите его, после того как выполните задание
if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 40)
    person.use_transport(car)
    print('=' * 40)
    person.use_transport(kamikadze)
