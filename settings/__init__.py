from .common import *
from .rest_framework import *
from .logging import *

try:
    from ._app import *
    assert DEBUG is False, "Never run on production with DEBUG = True!"
except NotImplementedError:
    from ._dev import *
