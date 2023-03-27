import importlib
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

wsgi = importlib.abc.ResourceLoader.load_module('wsgi', 'main.py')
application = wsgi.application