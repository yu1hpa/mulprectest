from mulprectest import *

# correct number of digits = 70
pi = "3141592653589793238462643383279502884197169399375105820974944592307816396"
mpt = Mulprectest(100, pi)
print(mpt.mulprectest()) # -> 70

pi_p = "3.14159265358979323846264338327950288419716939937510582097494459234"
mpt = Mulprectest(100, pi_p, False)
print(mpt.mulprectest()) # -> 65

