def fibonacci(n: int) -> int:
    '''
    Fast solution to find fibonacci number using Bine formula
    '''
    root_5 = 5**0.5
    return round((-1/root_5)*(((1-root_5)/2)**n)+(1/root_5)*(((1+root_5)/2)**n))


def fibonacci_recursive(n: int) -> int:
    '''
    Unoptimized solution to find fibonacci number using recursion
    '''
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
