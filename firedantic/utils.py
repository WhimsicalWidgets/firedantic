from typing import Iterator


def get_all_subclasses(cls) -> Iterator:
    """
    Recursively get all subclasses of a class.
    """
    for subclass in cls.__subclasses__():
        yield subclass
        yield from get_all_subclasses(subclass)


class classproperty:
    """
    A decorator that behaves like @property but for class methods.
    """

    def __init__(self, fget):
        self.fget = fget

    def __get__(self, owner, cls):
        return self.fget(cls)
