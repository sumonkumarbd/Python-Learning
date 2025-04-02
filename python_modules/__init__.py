print("\n $$$ Multi-file Module $$$ \n")

from .http_module import clientReq


__version__ ="1.0.0"
__author__ = "Sumonkmr"

def version():
    return __version__

def author():
    return __author__

