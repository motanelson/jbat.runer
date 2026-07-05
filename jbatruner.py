import jpype
import jpype.imports
import os
import copy
compilers="openjdk-asmtools-jasm $1.jbat -w . "
print("\033c\033[47;31m\ngive me file  jbat: to run ? \n")
#a="Hello.java"
a=input().strip()
b=a.replace(".jbat","")
os.system(compilers.replace("$1",b)  )
if not jpype.isJVMStarted():
    jpype.startJVM(classpath=["."])
Hello = jpype.JClass(b)

Hello.main([])

jpype.shutdownJVM()#a=input().strip()
