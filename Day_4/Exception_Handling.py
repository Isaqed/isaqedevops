from decimal import DivisionByZero
from logging import raiseExceptions
import builtins


cloud_ens=["AWS","Azure","GCP"]

try:
    print(cloud_ens[200])
    raise Exception  ("This is a new exception")
except:
    print("Exception Handled")
finally:
    print("I will execute anyway")

print("This code will run")

try:
    print(cloud_ens[200])
    a=10
    b=0
    c=a/b
except DivisionByZero as e:
    print("1",e)
except IndexError as e:
    print("2",e)

print(dir(builtins))


