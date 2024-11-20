from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FootnoteNumberFormat(Enum):
    """
    Specifies Numberformat of FootEndNote. 

    """
    Arabic = 0
    DecimalFullWidth = 14
    Hebrew1 = 45
    Hebrew2 = 47
    ArabicAlpha = 46
    ArabicAbjad = 48
    UpperCaseRoman = 1
    LowerCaseRoman = 2
    UpperCaseLetter = 3
    LowerCaseLetter = 4
    Chicago = 9
    ChineseLegalSimplified = 38
    ChineseCountingThousand = 39
    IdeographTraditional = 30
    IdeographZodiac = 31
    DecimalEnclosedCircleChinese = 28
    IdeographEnclosedCircle = 29
    none = 255

