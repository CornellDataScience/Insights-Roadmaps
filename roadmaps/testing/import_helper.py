
import sys
import os.path
import importlib

# `root` is completley dependent on where this file is in the project
root = os.path.abspath(os.path.join(os.path.dirname( __file__ ), os.pardir))
sys.path.insert(0, root)

def append_syspath(path):
    global root    
    package = os.path.abspath(os.path.join(root, path.replace('.', os.sep)))
    if os.path.isdir(package):
        sys.path.insert(0, package)
        return package

def import_modules(paths: list):
    for i in range(10):
        try:
            for path in paths:
                path = os.path.join()
                i = path.rfind('.')
                package, name = path[:i], path[i+1:]
                print(f'from {package} import {name}')

                importlib.import_module(name, package)
        except ModuleNotFoundError as e:
            print(i, e)
            append_syspath(os.path.dirname(e.name))
        


import_modules(['network.graph'])

print(graph.Graph())