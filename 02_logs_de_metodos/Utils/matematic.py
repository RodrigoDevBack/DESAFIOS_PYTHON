from Decorators.decorator_logins import decorator_log

class Serv:
    
    @decorator_log
    def sum(self, a, b):
        return a + b
    
    @decorator_log
    def fatorial(self, value):
        result = value
        for i in range(1, value):
            result *= i
        return result
    
    @decorator_log
    def fibonacci(self, limit):
        result = [0, 1]
        for i in range(1, limit+1):
            result.append(result[i] + result[i-1])
        return result
    