from functools import reduce


class Calculator:
    @staticmethod

    def add(*args):
        sum_values = sum(args)
        return sum_values

    @staticmethod
    def multiply(*args):
        multiplied_values = reduce(lambda a,b: a* b, args)
        return multiplied_values

    @staticmethod
    def divide( *args):
        divided_values = reduce(lambda a, b: a / b, args)
        return divided_values

    @staticmethod
    def subtract( *args):
        subtracted_values = reduce(lambda a, b: a - b, args)
        return subtracted_values






