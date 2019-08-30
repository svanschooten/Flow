from abc import ABCMeta, abstractmethod


class AbstractMethod:
    __metaclass__ = ABCMeta
    name = 'AbstractMethod'

    @staticmethod
    @abstractmethod
    def apply(args):
        """
        Apply the input signal dictionary and return a output signal dictionary
        """
        pass
