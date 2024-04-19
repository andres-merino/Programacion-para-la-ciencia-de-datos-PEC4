import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='PEC4',
      version='1.0',
      description='Resolución de PEC4',
      author='Andrés Merino',
      author_email='aemerinot@uoc.edu',
      packages=['PEC4'],
install_requires=required,
     )
