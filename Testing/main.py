
# see features/test.feature
# see steps/beahev_tests.py 


def incrementor(stride: int):
    def f(x: int):
        return stride + x 
    return f 

foo = incrementor(0)
print(foo(15))