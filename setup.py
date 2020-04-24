from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='game-grid',
    version='0.0.1',
    author='Cezar Azevedo de Faveri',
    description='Provides some utils to use grids mostly on games',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ChepChaf/grid',
    packages=['grid']
)
