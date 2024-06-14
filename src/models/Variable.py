import sympy as sp

class Variable(sp.Symbol):
    def __new__(cls, name, description, unit=1):
        obj = super().__new__(cls, name)
        obj.description = description
        obj.unit = unit
        obj._value = None
        return obj

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        if v is not None:
            self._value = v * self.unit