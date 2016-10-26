from distutils.core import setup


with open('README.rst') as f:
    long_description = f.read()


setup(
    name='ipython_unittest',
    version='0.0.1.dev',
    author='Antti Kaihola <antti dot kaihola at eniram dot fi>',
    py_modules=['ipython_unittest'],
    url='https://github.com/akaihola/ipython_unittest',
    license='README.rst',
    description='IPython extension to run a unittest suite for the current cell.',
    long_description=long_description,
)
