import re
import sympy
class Mulprectest:
    def __init__(self, digit: int, string: str, is_rm=True):
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
        self.is_rm = is_rm

    def mulprectest(self):
        PI = str(sympy.pi.evalf(self.digit))

        if(self.is_rm):
            rep_PI = PI.replace('.', '')
            for si in range(len(self.string)):
                if(rep_PI[si] != self.string[si]):
                    return si
        else:
            for si in range(len(self.string)):
                if(PI[si] != self.string[si]):
                    return si - 1
