import os
import copy
compilers="openjdk-asmtools-jasm $1.jbat -w . "
print("\033c\033[47;31m\ngive me file  jbat: to run ? \n")
#a="Hello.java"
a=input().strip()
b=a.replace(".jbat","")
os.system(compilers.replace("$1",b)  )
os.system("java $1".replace("$1",b))