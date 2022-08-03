from functools import wraps


class FunctionalInterface:
    def __init__(self, function, /, *args, **kwargs):
        self._name = None
        self.function = function
        wraps(self.function)(self)
        self.function_mehtods = [name for name in dir(function) if callable(getattr(function, name)) and not name.startswith('__')]
    
    def __set_name__(self, owner, name):
        self._name = name
        
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    
    def __set__(self, instance, value):
        instance.__dict__[self._name] = value
        for method in self.function_mehtods:
            setattr(instance.__dict__[self._name], method, instance.__dict__[self._name])
            
    def __call__(self, *args, **kwargs):
        return self.__class__(self.function, *args, **kwargs)

@FunctionalInterface
class Command:
    def execute(self) -> None:
        pass