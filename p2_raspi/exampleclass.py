#Einfache Klasse, die getestet werden soll
#@author Jan Strothmann

class ExampleClass:

    def __init__(self,multiplicator):
        self.inner_val=1
        self.multi=multiplicator

    def compute(self,outer_val):
        return self.inner_val*self.multi*outer_val


