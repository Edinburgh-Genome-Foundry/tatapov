import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

exec(open('tatapov/version.py').read()) # loads __version__

setup(
    name='tatapov',
    version=__version__,
    author='Zulko',
    description='Provides DNA overhang misannealing data (Potatov 2018).',
    long_description=open('README.rst').read(),
    license='see LICENSE.txt',
    keywords="overhang golden gate dna annealing mismatch potapov",
    packages=find_packages(exclude='docs'),
    include_package_data=True,
    install_requires=["pandas", "appdirs", "flametree"])
