from unittest import TestCase, TestLoader, TestSuite, TextTestRunner

import types
from IPython.core import magic


def unittest(line, cell):
    test_module = types.ModuleType('test_module')
    test_module.__dict__.update(get_ipython().user_ns)
    exclude = dir(test_module)
    exec(cell, test_module.__dict__)
    suite = TestSuite()
    loader = TestLoader()
    for name in dir(test_module):
        if name not in exclude:
            obj = getattr(test_module, name)
            if isinstance(obj, type) and issubclass(obj, TestCase):
                suite.addTest(loader.loadTestsFromTestCase(obj))
    TextTestRunner(verbosity=2).run(suite)


def load_ipython_extension(ipython):
    magic.register_cell_magic(unittest)
