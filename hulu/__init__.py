#    __  __   __  __   __       __  __
#   /\ \_\ \ /\ \/\ \ /\ \     /\ \/\ \
#   \ \  __ \\ \ \_\ \\ \ \____\ \ \_\ \
#    \ \_\ \_\\ \_____\\ \_____\\ \_____\
#     \/_/\/_/ \/_____/ \/_____/ \/_____/

"""
hulu
----

hulu is a Python library to help developers interact with Hulu's "hidden" API.
"""

__author__ = 'Mike Helmick'
__version__ = '0.1.0'

from .api import Hulu
from .exceptions import HuluError
