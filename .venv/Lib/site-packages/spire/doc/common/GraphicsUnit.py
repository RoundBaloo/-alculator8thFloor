from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
if __package__ == "spire.pdf.common":
    from spire.pdf.common import *
elif __package__ == "spire.xls.common":
    from spire.xls.common import *
elif __package__ == "spire.doc.common":
    from spire.doc.common import *
else :
    from spire.presentation.common import *
#from spire.xls import *
from ctypes import *
import abc

class GraphicsUnit(Enum):
    """

    """
    World = 0
    Display = 1
    Pixel = 2
    Point = 3
    Inch = 4
    Document = 5
    Millimeter = 6

