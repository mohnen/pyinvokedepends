__version__ = "0.0.5"
from invoke import tasks

import warnings
import os
import glob

def depends(*args, **kvargs):
    """ A decorator for invoke's task decoration, which only executes the task when file changes have occured. """
    class decorator(tasks.Task):
        """ The decorator class """
        def __init__(self, func):
            super().__init__(func)
            self.func = func

        def __call__(self, *args, **kwargs):
            """ Performs the actual execution """
            callthetask = True
            on = [os.path.getmtime(path) for pattern in kvargs['on'] for path in glob.glob(pattern)]
            if len(on)==0:
                raise ValueError("none of files in on exist", kvargs['on'])
            creates = [os.path.getmtime(path) for pattern in kvargs['creates'] for path in glob.glob(pattern)]
            if len(creates)!=0:
                callthetask = max(on)>=min(creates)
            if callthetask:
                return self.func(*args, **kwargs)
            print('Not calling {func}'.format(func=self.func.__name__))
            return None

    if len(args)>0:
        if not isinstance(args[0], tasks.Task) or len(args)!=1:
            raise ValueError("@depends only possible with kwargs")
        warnings.warn('@depends without arguments will do nothing', SyntaxWarning)
        kvargs['on']=['.']
        kvargs['creates']=['.']
        return decorator(args[0])
    n = len({'on', 'creates'}.intersection(set(kvargs.keys())))
    if n in (2,0):
        if n==0:
            warnings.warn('@depends without "on" and "creates" will do nothing', SyntaxWarning)
            kvargs['on']=['.']
            kvargs['creates']=['.']
        return decorator
    raise ValueError('@depends needs both "on" and "creates"')
