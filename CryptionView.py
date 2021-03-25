#TESTING SCRIPT
import sys
import os
from os import listdir
import pathlib
from os.path import isfile, join

currentDirectory=os.path.dirname(os.path.abspath(__file__))

files = [f for f in listdir(currentDirectory) if isfile(join(currentDirectory,f))]
directories = [d for d in listdir(currentDirectory) if not isfile(join(currentDirectory,d))]

print("**************FILES**************")
for i in range(len(files)):
    print(str(i) + ") " + files[i] )
print("***********DIRECTORIES***********")
for i in range(int(len(files)), int(len(files) + len(directories))):
    print(str(i) + ") " + directories[i-len(files)] )
print("PODAJ LICZBE")


x = input()
print(x)
print(len(files))
if len(files)>int(x):
    print("Wybrany plik: " + files[int(x)])
elif len(files)<=int(x):
    print("Wybrany katalog: " + directories[int(x)-len(files)])
#END TESTING SCRIPT