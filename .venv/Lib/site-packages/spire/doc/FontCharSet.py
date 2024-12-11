from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FontCharSet(Enum):
    """
    Enumeration of font character sets.
    """
    ANSI_CHARSET = 0
    DEFAULT_CHARSET = 1
    SYMBOL_CHARSET = 2
    SHIFTJIS_CHARSET = 128
    HANGEUL_CHARSET = 129
    HANGUL_CHARSET = 129
    GB2312_CHARSET = 134
    CHINESEBIG5_CHARSET = 136
    OEM_CHARSET = 255
    JOHAB_CHARSET = 130
    HEBREW_CHARSET = 177
    ARABIC_CHARSET = 178
    GREEK_CHARSET = 161
    TURKISH_CHARSET = 162
    VIETNAMESE_CHARSET = 163
    THAI_CHARSET = 222
    EASTEUROPE_CHARSET = 238
    RUSSIAN_CHARSET = 204
    MAC_CHARSET = 77
    BALTIC_CHARSET = 186
