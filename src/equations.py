from variables import *
import sympy as sp

# Bernoulli no escoamento permanente (1.11a)
eq_bernoulli = sp.Eq(pa/gama + za + va**2/(2*g), pb/gama + zb + vb**2/(2*g) + delta_h)

# Cotas piezométricas (1.11x)
eq_cpa = pa/gama + za
eq_cpb = pb/gama + zb