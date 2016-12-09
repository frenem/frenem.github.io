#!/bin/python

from time import *
import datetime
from multiprocessing.dummy import Pool


def timer(f):
        def wrapper(*args,**kwargs):
                start = datetime.datetime.now()
                f(*args,**kwargs)
                args = list(args)
                print("Temps d'execution avec %d thread : %s " % (args[0], datetime.datetime.now()-start) )

        return wrapper

def slow_operation(n):
        sleep(n)
#       print('Slow Operation %d complete.' % n )

@timer
def main():
        slow_operation(1)
        slow_operation(2)
        slow_operation(3)

@timer
def m(k):
        pool = Pool(k)
        result = pool.map(slow_operation,range(1,7))
        pool.close()
        pool.join()



map(m,range(1,11))
