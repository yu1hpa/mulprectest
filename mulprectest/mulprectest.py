import re
import sympy
class Mulprectest:
    def __init__(self, digit: int, string: str):
        """
        Args:
            digit   (int): The PI size
            string  (str): The strings gotten from stdout
            is_rm   (bool): The flag whether or not remove the (dec) point

        Returns:
            int:    Number of digits matched
        """

        self.digit = digit
        self.string = string
        self.is_rm = ('.' not in self.string)

    def mulprectest(self):
        PI = str(sympy.pi.evalf(self.digit))

        if(self.is_rm):
            rep_PI = PI.replace('.', '')
            for si, is_last in self.last(range(len(self.string))):
                if(rep_PI[si] != self.string[si]):
                    return si
                if(is_last):
                    return si + 1
        else:
            for si, is_last in self.last(range(len(self.string))):
                if(PI[si] != self.string[si]):
                    return si - 1
                if(is_last):
                    return si

    def last(self, iterable):
        """
        Args:
            iterable    (iter): The iterator

        Return:
            is_last     (bool): Last or not
        """
        it = iter(iterable)
        last = next(it)
        for val in it:
            yield last, False
            last = val

        yield last, True
