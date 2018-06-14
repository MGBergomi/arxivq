import os
import sys
from distutils.sysconfig import get_python_lib
from setuptools import find_packages, setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This code has been tested on Python {}.{}, it could fail on Python {}.{}.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

EXCLUDE_FROM_PACKAGES = []

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name='ArxivQ',
    version='0.1.0',
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
    author='Mattia G Bergomi',
    author_email='mattia.bergomi@neuro.fchampalimaud.org',
    description=('A simple class to plot and fit histogram drawn from '
                 'ArXiv data, based on publication and update dates'),
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    install_requires=['numpy',
                      'pandas',
                      'matplotlib',
                      'seaborn',
                      'scipy'],
    # dependency_links=['git+https://github.com/lukasschwab/arxiv.py.git@master#egg=arxiv.py-0'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
    ],
    project_urls={
        'Source': 'https://github.com/MGBergomi/ArxivQ',
    },
)
