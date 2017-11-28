from setuptools import setup, Extension, find_packages

ext_mod = Extension("_rundec",
                    sources=["_rundec.cc", "CRunDec3/CRunDec.cpp"],
                    )

setup(name="rundec",
      version="0.0.1",
      author="David M. Straub",
      author_email="david.straub@tum.de",
      url="https://github.com/DavidMStraub/rundec-python",
      description="A Python wrapper around the CRunDec package for the "
                  " running and decoupling of the strong coupling constant "
                  "and quark masses",
      long_description="""`CRunDec` is a C++ program developed by
      Florian Herren and Matthias Steinhauser. This Python package
      provides a thin wrapper around `CRunDec` generated with SWIG.""",
      license="GPLv3",
      packages=find_packages(),
      ext_modules=[ext_mod],
      )
