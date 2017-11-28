# rundec-python

`CRunDec` is "a C++ program for the running and decoupling of the strong coupling constant and quark masses", developed by Florian Herren and Matthias Steinhauser. Relevant references:

- "Version 3 of RunDec and CRunDec",
Florian Herren, Matthias Steinhauser
[arXiv:1703.03751](https://arxiv.org/abs/1703.03751)
- "CRunDec: a C++ package for running and decoupling of the strong coupling and quark masses",
Barbara Schmidt, Matthias Steinhauser
[arXiv:1201.6149](https://arxiv.org/abs/1201.6149)
- "RunDec: A Mathematica package for running and decoupling of the strong coupling and quark masses",
K.G. Chetyrkin, Johann H. Kühn, M. Steinhauser
[arXiv:hep-ph/0004189](https://arxiv.org/abs/hep-ph/0004189)

[Source code of CRunDec 3.0](https://www.ttp.kit.edu/preprints/2017/ttp17-011)

`rundec-python` is a Python package providing a thin wrapper around `CRunDec`.

## Installation

```bash
pip install rundec
```

## Usage

The API is analogous to `CRunDec`, see [the documentation](https://arxiv.org/abs/1703.03751).

```python
import rundec

crd = rundec.CRunDec()

# compute alpha_s at the b quark mass scale with 3-loop accuracy
crd.AlphasExact(0.1185, 91.1876, 4.18, 5, 3)

# compute the b quark pole mass using the 2-loop conversion from the MSbar mass
crd.mMS2mOS(4.18, None,  0.26, 4.18, 5, 2)
```

## Technical details

The wrapper was generated with [SWIG](http://www.swig.org/).

Binary wheels are provided via [PyPI](https://pypi.python.org/pypi/rundec) for Linux and Mac OS (built on [Travis CI](https://travis-ci.org/)) and for Windows (built on [AppVeyor](https://www.appveyor.com/)).

The Windows wheels require Python 3.5+, on Linux and Mac OS Python 2.7+ is sufficient.
