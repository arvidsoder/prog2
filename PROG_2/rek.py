

def factorial(inte:int) -> int:
    if inte > 0:
        return inte*factorial(inte-1)
    else:
        return 1
    
print(factorial(6))