from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PdfConformanceLevel(Enum):
    """
    Specifies the Pdf document's Conformance-level.
    """
    none = 0
    Pdf_A1B = 1
    Pdf_X1A2001 = 2
    Pdf_A1A = 3
    Pdf_A2A = 4
    Pdf_A2B = 5
    Pdf_A3A = 6
    Pdf_A3B = 7
