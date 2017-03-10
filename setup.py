# Standard library imports ...
import os
import re
import sys

# Third party library imports ...
from setuptools import setup

kwargs = {
    'name': 'ideal_octo_parakeet',
    'author': 'John Evans',
    'author_email': 'john.g.evans.ne@gmail.com',
    'url': 'https://github.com/quintusdias/ideal-octo-parakeet',
    'packages': ['ideal_octo_parakeet'],
    'entry_points': {
        'console_scripts': ['gbdump=ideal_octo_parakeet.commandline:gbdump'],
    },
    'license': 'MIT',
}

setup(**kwargs)
