import ez_setup

ez_setup.use_setuptools()

from setuptools import setup, find_packages

exec(open("tatapov/version.py").read())  # loads __version__

setup(
    name="tatapov",
    version=__version__,
    author="Zulko",
    url="https://github.com/Edinburgh-Genome-Foundry/tatapov",
    description="Provides DNA overhang misannealing data (Potapov 2018).",
    long_description=open("pypi-readme.rst").read(),
    license="MIT",
    keywords="overhang golden gate dna annealing mismatch potapov",
    packages=find_packages(exclude="docs"),
    include_package_data=True,
    install_requires=["pandas", "appdirs", "flametree", "xlrd<2"],
)
