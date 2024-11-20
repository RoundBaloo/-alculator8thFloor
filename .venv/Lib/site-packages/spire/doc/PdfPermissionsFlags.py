from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PdfPermissionsFlags(Enum):
    """
    Specifies the available permissions set for the signature.
    """
    none = 0
    Default = 2876
    Print = 4
    EditContent = 8
    CopyContent = 16
    EditAnnotations = 32
    FillFields = 256
    AccessibilityCopyContent = 512
    AssembleDocument = 1024
    FullQualityPrint = 2244

