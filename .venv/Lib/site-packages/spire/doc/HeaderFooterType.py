from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class HeaderFooterType(Enum):
    """
    Specifies type of the Header/Footer.
    """
    HeaderEven = 0
    HeaderOdd = 1
    FooterEven = 2
    FooterOdd = 3
    HeaderFirstPage = 4
    FooterFirstPage = 5

