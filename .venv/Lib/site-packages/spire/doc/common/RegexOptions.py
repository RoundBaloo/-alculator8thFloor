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
from ctypes import *
import abc

class RegexOptions(Enum):
    """

    """
    none = 0
    IgnoreCase = 1
    Multiline = 2
    ExplicitCapture = 4
    Compiled = 8
    Singleline = 16
    IgnorePatternWhitespace = 32
    RightToLeft = 64
    ECMAScript = 256
    CultureInvariant = 512

