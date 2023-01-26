#LoggerThingie.py
import functools
from textwrap import wrap
class LoggerThingie(object):
    def __init__(self,fname):
         self.file = open(fname,mode)
         self.file.write("")
    
    #@gfg_openfile
    def openfile(func):
        
        def wrapper(*args, **kwargs):
        
            file = open(fname, mode)
            print("openened")
            file=func(file,mode)
            return file,func
        return wrapper

    """"def modifyfile(func):
        def wrapper2(file,*args, **kwargs):
        
            func(file)
            file.close()
            print("modified")
            return file
        return wrapper2"""""

    
    #@modifyfile
    @openfile
    def fread(file,mode):
        file=file
        mode=mode
        file.read()

    #@modifyfile
    @openfile
    def fwrite(file,mode,args): file.write(mode,args)
    
    #@modifyfile
    @openfile
    def freadlines(file,mode): file.readlines()
    
    #@modifyfile
    @openfile
    def fwritelines(file,mode,args): file.writelines(mode, args)
    #fread = openfile(fread)

fname="filetest.txt"
mode="r"
a=str(LoggerThingie.fread(fname,mode))
print(a)
print("done")
while 1:
    continue




"""
from functools import partial

def _pseudo_decor(fun, argument):
    def ret_fun(*args, **kwargs):
        #do stuff here, for eg.
        print ("decorator arg is %s" % str(argument))
        return fun(*args, **kwargs)
    return ret_fun

real_decorator = partial(_pseudo_decor, argument=arg)

@real_decorator
def foo(*args, **kwargs):
    pass

"""
