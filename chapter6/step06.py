import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        self.intput = input #入力された変数を覚える
        return output
    
    #順伝播
    def forward(self, x):
        raise NotImplementedError()
    
    #微分の計算を行う逆伝播
    def backward(self,gy):
        raise NotImplementedError()
    

class Square(Function):

    def forward(self, x):
        return x ** 2
    
    def backward(self,gy):
        x = self.input.data
        gx = 2*x*gy
        return gx

class Exp(Function):

    def forward(self, x):
        y = x**2
        return np.exp(x)

    def backward(self, gy):
        x =self.input.data
        gx = np.exp(x)*gy
        return gx
    

    
def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2 * eps)

def f(x):
    A = Square()
    B = Exp()
    C = Square()
    return C(B(A(x)))



