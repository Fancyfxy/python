def test(func):
    def new_func(*args,**kwargs):
        print('start')
        result=func(*args,**kwargs)
        print('end')
        return result
    return new_func
@test
def add(a,b):
    print(a+b)

add( 1 , 2)
class OopsException(Exception):
    pass

try :
    raise OopsException
except OopsException:
    print ('sd')
title=['1','2']
plots=['1','2']
movi=dict(zip(title,plots))
print(movi)