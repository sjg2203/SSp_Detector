import logging
import os
from .ssp_detector import *
from outdated import warn_if_outdated
path=os.path.abspath(os.path.dirname(__name__))

#Define logger
logging.basicConfig(format='%(asctime)s|%(levelname)s|%(message)',datefmt='%y-%b-%d %H:%M:%S')

__author__='Simon J. Guillot <simon.guillot@inserm.fr>'
VERSION=''
DISTNAME='SSp_Detector'
about={}
if not VERSION:
    pr=DISTNAME.lower().replace("-","_").replace(" ","_")
    with open(os.path.join(path,pr,'SSp_Detector\__version__.py')) as f:
        exec(f.read(),about)
else:
    about['__version__']=VERSION
__version__=about['__version__']

#Warn if newer version is available
warn_if_outdated('SSp_Detector',__version__)
