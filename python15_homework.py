from loguru import logger
import argparse

# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
# больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно
# сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
class TriangleChecker:
    """Внутри класса идет логгирование и запись логов в файл"""
    def __init__(self, a: int, b: int, c: int) -> None:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            logger.error('Only int or float numbers allowed')
            logger.add('craft.log', format='{time}, {level}, {message}', level='DEBUG', rotation='10:00')
            raise TypeError('Only int or float numbers allowed')
        elif a > c + b or b > a + c or c > b + a:
            logger.error('No triangle with these sides is possible')
            logger.add('craft.log', format='{time}, {level}, {message}', level='DEBUG', rotation='10:00')
            raise ValueError('No triangle with these sides is possible')
        else:
            self.a = a
            self.b = b
            self.c = c
            logger.info('This triangle can exist')
            logger.add('craft.log', format='{time}, {level}, {message}', rotation='10:00')

    def get_sides(self):
        return self.a, self.b, self.c

    def is_isosceles(self) -> str:
        """Проверка на равнобедренность"""
        if (self.a == self.b and self.b != self.c and self.a != self.c) or (
                self.c == self.b and self.b != self.a and self.c != self.a):
            logger.info('Triangle is isosceles')
            logger.add('craft.log', format='{time}, {level}, {message}', rotation='10:00')
            return f'Triangle is isosceles'
        else:
            logger.error('Triangle is not isosceles')
            logger.add('craft.log', format='{time}, {level}, {message}', level='DEBUG', rotation='10:00')
            return f'Triangle is not isosceles'

    def is_fullside(self) -> str:
        """Проверка на равносторонность"""
        if self.a == self.b == self.c:
            logger.info('Triangle is fullside')
            logger.add('craft.log', format='{time}, {level}, {message}', rotation='10:00')
            return f'Triangle is fullside'
        else:
            logger.error('Triangle is not fullside')
            logger.add('craft.log', format='{time}, {level}, {message}', level='DEBUG', rotation='10:00')
            return f'Triangle is not fullside'

    @staticmethod
    def do_parsing():
        parser = argparse.ArgumentParser(description='hometask_final')
        parser.add_argument('-p', metavar='path', type=str, nargs='*', default='|', help='Put your path here')
        args = parser.parse_args()
        return args.p


# Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
class Animal:
    def __init__(self, species: str) -> None:
        self.species = species
        logger.info('Initial class has been created')
        logger.add('animals.log', format='{time}, {level}, {message}')

    def class_parser(self):
        parser = argparse.ArgumentParser(description='hometask_final')
        parser.add_argument('-a', metavar='path', type=str, nargs='*', default='|', help='Put your data here')
        args = parser.parse_args()
        return args.a


class Turtle(Animal):
    def __init__(self) -> None:
        super().__init__('Turtle')
        logger.info('Initial class has been created')
        logger.add('animals.log', format='{time}, {level}, {message}')

    def class_parser(self):
        super().class_parser()


class Dinosaur(Animal):
    def __init__(self) -> None:
        super().__init__('Dinosaur')
        logger.info('Initial class has been created')
        logger.add('animals.log', format='{time}, {level}, {message}')

    def class_parser(self):
        super().class_parser()


class AnimalFabric:

    @staticmethod
    def create_animal(animal_species: str):
        if animal_species == 'Turtle':
            return Turtle()
        elif animal_species == 'Dinosaur':
            return Dinosaur()
        else:
            logger.error('No such animal is allowed')
            logger.add('craft.log', format='{time}, {level}, {message}', level='DEBUG')
            return f'Wrong animal species'