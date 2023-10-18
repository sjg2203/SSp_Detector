# Sleep Spindles Detector

[![GitHub release](https://img.shields.io/github/release/sjg2203/SSp_Detector)](https://GitHub.com/sjg2203/SSp_Detector/releases/) [![PyPI pyversions](https://img.shields.io/pypi/pyversions/SSp_Detector.svg)](https://pypi.python.org/pypi/SSp_Detector)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/sjg2203/SSp_Detector/LICENSE) [![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit) [![HitCount](https://hits.dwyl.com/sjg2203/SSp_Detector.svg)](https://hits.dwyl.com/sjg2203/SSp_Detector)

[Sleep Spindles Detector](https://github.com/sjg2203/SSp_Detector) toolbox analyse raw EEG signals to then extrapolate the number of sleep spindles using either the absolute or relative Sigma power (11-16Hz).

The toolbox is optimised for Python 3.10 and above and was tested on both Windows and macOS ARM.

*All dependencies are listed in [requirements](requirements.txt).

## Contribution [![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/sjg2203/SSp_Detector/issues)

These pipelines were created and is maintained by SJG.

Contributions are more than welcome so feel free to submit a [pull request](https://github.com/sjg2203/SSp_Detector/pulls)!

To report a bug, please open a new [issue](https://github.com/sjg2203/SSp_Detector/issues).

Note that this program is provided with NO WARRANTY OF ANY KIND under Apache 2.0 [license](LICENSE).


## Installation of Python package
To install the toolbox, simply use:

- Using conda

```python
conda install -c conda-forge ssp_detector
```

- Using pip

```python
pip install ssp_detector
```

Everything worked if the following command do not return any error:

```python
import ssp_detector
```

## Citation

To cite this toolbox, please use the following:

 - Simon J Guillot, Sleep Spindles Detector toolbox (version "build_number", https://github.com/sjg2203/SSp_Detector) in Python.
