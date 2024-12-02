#!/usr/bin/env python3

def check_exact_obj(obj, class_):
    return type(obj) is class_
    
if __name__=="__main__":
    class Base:
        pass
    b = Base()
    i = [1, 2]
    for x in [b, i]:
        if check_exact_obj(x, int):
            print(f"{x} is an instance of class {int.__name__}")
        if check_exact_obj(x, list):
            print(f"{x} is an instance of class {list.__name__}")
        if check_exact_obj(x, Base):
            print(f"{x} is an instance of class {Base.__name__}")
        if check_exact_obj(x, object):
            print(f"{x} is an instance of class {object.__name__}")
