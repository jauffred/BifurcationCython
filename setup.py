from distutils.core import setup
from Cython.Build import cythonize

setup(name="BifurcationCy",
      ext_modules=cythonize("BifurcationCy.pyx"))
