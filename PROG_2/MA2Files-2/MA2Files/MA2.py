"""
Solutions to module 2 - A calculator
Student: Arvid Söderström
Mail: arvid.s@live.se
Reviewed by:Andrey Shternshis
Reviewed date:
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""
#import numpy
import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper


        
class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg) -> None:
        self.arg = arg
        super().__init__(self.arg)

def sum2(*arg): 
    return sum(arg)
def fac2(n):
    if n//1 == n:
        try:
            return math.factorial(int(n))
        except ValueError as ve:
            raise EvaluationError(ve)
    else:
        raise EvaluationError("Factorial is only defined for integers")
def logE(arg):
    if arg <= 0:
        raise EvaluationError("Logaritm undefined for 0 and negative numbers")
    else:
        return math.log(arg)

def fibonacci(n):
    memory = {0:0, 1:1}
    def _fib(n):
        if n < 0:
            raise EvaluationError(f"Argument to fib is {n}. Must be integer >= 0")
        if n not in memory:
            memory[n] = _fib(n-1) + _fib(n-2)
        return memory[n]
    return _fib(n)

def mean_value(*arg):
    return sum(arg)/len(arg)

def standard_dev(*arg):
    mu = mean_value(*arg)
    dev = tuple(map(lambda x: (x - mu)**2, arg))
    return math.sqrt(mean_value(*dev))

def statement(wtok, variables):
    """ See syntax chart for statement"""
    if wtok.is_at_end():
        result = 0
    else:
        result = assignment(wtok, variables)
        if not (wtok.is_at_end()):
            raise SyntaxError("There are more characters on the line")
    return result

def assignment(wtok, variables: dict):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables.update({wtok.get_current(): result})
            wtok.next()
        else:
            raise SyntaxError("The equals sign was not followed by a variable name")
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while (wtok.get_current() == '+') or (wtok.get_current() == '-'):
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        elif wtok.get_current() == '-':
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while (wtok.get_current() == '*') or (wtok.get_current() == '/'): 
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables)
        elif wtok.get_current() == '/':
            wtok.next()
            denominator = factor(wtok, variables)
            try:
                result = result / denominator
            except ZeroDivisionError as zeroerror:
                raise EvaluationError(zeroerror)
    return result

def arglist(wtok, variables):
    if wtok.get_current() == '(':
        wtok.next()
        args = argrekur(wtok, variables)
    else:
        raise SyntaxError("Expected '('")

    return args

def argrekur(wtok, variables):
    arg = assignment(wtok, variables)
    if wtok.get_current() == ')':
        wtok.next()
        return [arg]
    elif wtok.get_current() == ',':
        wtok.next()
        return [arg] + argrekur(wtok, variables)
    else: 
        raise SyntaxError("Expected ',' or ')'")

def factor(wtok, variables):
    """ See syntax chart for factor"""


    function_1 = {'sin' : math.sin, 'cos': math.cos,
                  'exp' : math.exp, 'log': logE, 
                  'fac' : fac2, 'fib': fibonacci}
    function_N = {'max': max, 'min': min, 'sum': sum2, 'mean': mean_value, 'std': standard_dev}
    factor_first = wtok.get_current()

    if factor_first == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    elif factor_first in function_1:
        current_function = wtok.get_current()
        wtok.next()
        if wtok.get_current() == '(':
            wtok.next()
            result = function_1[current_function](assignment(wtok, variables))
            if wtok.get_current() != ')':
                raise SyntaxError("Expected ')'")
            else:
                wtok.next()
        else:
            raise SyntaxError("Expected '(' after the function")
    
    elif factor_first in function_N:
        current_function = wtok.get_current()
        wtok.next()
        result = function_N[current_function](*arglist(wtok, variables))

    elif factor_first in variables:
        result = variables[wtok.get_current()]
        wtok.next()

    elif factor_first == 'j':
        result = 1j
        wtok.next()

    elif wtok.is_name():
        raise EvaluationError("Unknown variable or function")

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif factor_first == '-':
        wtok.next()
        result = -factor(wtok, variables)

    else:
        raise SyntaxError("Expected number, variable , function or '('")  
    return result

def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)
        
            
        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            print('Variables\n')
            for k, v in variables.items():
                print(f'{k}\t: {v}')
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Token error: Unbalanced parentheses')
            
            except EvaluationError as ee:
                print("*** Evalutation error: ", ee)



if __name__ == "__main__":
    main()
