import numpy as np

class Variable:
    def __inint__(self,data):
        self.data = data

class Function:
    def __call__(self,init):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output
    
    def forward(self,x):
        raise x**2
    

x= Variable(np.array(10))
f = Function()
y=f(x)

print(type(x))
print(y.data)