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

class PixelFormat(Enum):
    """

    """
    Indexed = 65536
    Gdi = 131072
    Alpha = 262144
    PAlpha = 524288
    Extended = 1048576
    Canonical = 2097152
    Undefined = 0
    DontCare = 0
    Format1bppIndexed = 196865
    Format4bppIndexed = 197634
    Format8bppIndexed = 198659
    Format16bppGrayScale = 1052676
    Format16bppRgb555 = 135173
    Format16bppRgb565 = 135174
    Format16bppArgb1555 = 397319
    Format24bppRgb = 137224
    Format32bppRgb = 139273
    Format32bppArgb = 2498570
    Format32bppPArgb = 925707
    Format48bppRgb = 1060876
    Format64bppArgb = 3424269
    Format64bppPArgb = 1851406
    Max = 15

