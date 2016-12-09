#! /bin/python

def deco(f):
        def wrapper():
                print("in the wrapper")
                f()

        return wrapper
@deco
def fnct():
        print("in my fonction")


fnct()
