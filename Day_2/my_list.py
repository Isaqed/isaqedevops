from os import lstat
from re import L


list_of_linux=list(["Fedora","RedHat","Centos"])
list_of_linux=["Fedora","RedHat","Centos"]
list_of_linux.append("SUSE")
list_of_linux.insert(0,"Ethium")
for i in list_of_linux:
    print("Working on ",i)
print(dir(list_of_linux))
print(list_of_linux.index.__doc__)

    