import setuptools

__version__ = "1.0.0"

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='gregorian-months',
    version=__version__,
    long_description=long_description,
    description='Conduct with the Gregorian calendar months',
    author='Iftah Roichman',
    url='https://github.com/iftahro/gregorian-months',
    packages=setuptools.find_packages()
)
