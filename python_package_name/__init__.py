"""
@author: Gabriele Girelli
@contact: gigi.ga90@gmail.com
"""

from python_package_name import something

from importlib.metadata import version

try:
    __version__ = version(__name__)
except Exception as e:
    raise e

__all__ = [
    "__version__",
]
