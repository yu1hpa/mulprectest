import re
import sympy
class Mulprectest:
    def __init__(self, digit: int, approx_pi: str):
        """
        Args:
            digit   (int): The PI size
            approx_pi  (str): The strings gotten from stdout
            is_rm   (bool): The flag whether or not remove the (dec) point

        Returns:
            int:    Number of digits matched
        """

        self.digit = digit
        self.approx_pi = approx_pi
        self.is_rm = ('.' not in self.approx_pi)

    def mulprectest(self):
        PI = str(sympy.pi.evalf(self.digit))

        if(self.is_rm):
            rep_PI = PI.replace('.', '')
            for si, is_last in self.last(range(len(self.approx_pi))):
                if(rep_PI[si] != self.approx_pi[si]):
                    return si
                if(is_last):
                    return si + 1
        else:
            for si, is_last in self.last(range(len(self.approx_pi))):
                if(PI[si] != self.approx_pi[si]):
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
