from equations import *
from variables import *
import models.Variable
import sympy as sp

sp.init_printing(use_unicode=True)

def solve(equation, dependant_variable = None):
    variables_set = (equation.lhs.free_symbols.union(equation.rhs.free_symbols))
    if dependant_variable == None:
        dependant_variable = choose_dependant_variable(variables_set)
    variables_set.remove(dependant_variable) # Resulta no set das variáveis independentes
    independant_variables_list = list(dict.fromkeys(variables_set))

    symbolic_solution = sp.solve(equation, dependant_variable)
    sp.pprint(symbolic_solution)

    for var in independant_variables_list:
        # input_value = input(f"Insira o valor da variável {var} ({var.unit}): ")
        # var.value = sp.sympify(input_value)
        var.value = get_input_value(var)

    substituted_equation = equation.subs({var: var.value for var in independant_variables_list})

    solution = sp.solve(substituted_equation, dependant_variable)
    sp.pprint(solution)
    
    return solution

def choose_dependant_variable(variable_set):
    for var in variable_set:
        choice = input(f"Escolher a variável {var.name}? (s)/(n): ")
        if choice.lower() == "s":
            return var
    
    raise Exception("Nenhuma variável foi escolhida.")

def get_input_value(variable):
    if variable.name == 'zᴀ':
        return 90
    elif variable.name == 'zʙ':
        return 75
    elif variable.name == 'pᴀ':
        return 275000
    elif variable.name == 'pʙ':
        return 345000
    elif variable.name == 'vᴀ':
        return 1.98
    elif variable.name == 'vʙ':
        return 1.98
    elif variable.name == 'γ':
        return 9810
    elif variable.name == 'g':
        return 9.81
    elif variable.name == 'ΔH':
        return 7.86
    else:
        return None

solve(eq_bernoulli)