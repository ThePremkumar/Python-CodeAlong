# OOPS conpect 
# only using the Class

class CalculatorOperation:

    def __init__(self, a , b):
        self.a = a
        self.b = b

    def additional(self):
        try:
            c = self.a + self.b
            print("The total is: ", c)
        except Exception as error:
            print(error)

    def subtraction(self):
        try:
            if self.a > self.b:
                sub = self.a - self.b
                print("The Subtraction value is:" ,sub)
            else:
                sub = self.b - self.a
                print("The Subtraction value is:" ,sub)
        except Exception as error:
            print(error)
    

cal_opt=CalculatorOperation(15,20)
cal_opt.additional()
