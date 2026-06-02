def process(a:int):
     print(a)


def fors(froms:int,into:int,steep:int,procs):
    
    while froms <into:
         procs(froms)
         froms=froms+steep

_restarts={'fromm':0,'intos':10 , 'steeps':1}
_v=vars()
_v.update(_restarts)
fors(fromm,intos,steeps,process)