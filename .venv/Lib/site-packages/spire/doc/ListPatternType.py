from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ListPatternType(Enum):
    """
    Specifies type of the list numbering format.
    """
    Arabic = 0
    UpRoman = 1
    LowRoman = 2
    UpLetter = 3
    LowLetter = 4
    Ordinal = 5
    CardinalText = 6
    OrdinalText = 7
    Chicago = 9
    DecimalFullWidth = 14
    DecimalHalfWidth = 15
    Hebrew1 = 45
    ArabicAlpha = 46
    Hebrew2 = 47
    ArabicAbjad = 48
    JapaneseCounting = 11
    JapaneseLegal = 16
    JapaneseDigitalTenThousand = 17
    DecimalEnclosedCircle = 18
    DecimalFullWidth2 = 19
    LeadingZero = 22
    Bullet = 23
    DecimalEnclosedFullstop = 26
    DecimalEnclosedParen = 27
    DecimalEnclosedCircleChinese = 28
    KoreanDigital = 41
    KoreanCounting = 42
    KoreanLegal = 43
    KoreanDigital2 = 44
    AiueoFullWidth = 20
    Aiueo = 12
    Iroha = 13
    IdeographDigital = 10
    IrohaFullWidth = 21
    IdeographTraditional = 30
    IdeographZodiac = 31
    IdeographEnclosedCircle = 29
    IdeographZodiacTraditional = 32
    TaiwaneseCounting = 33
    IdeographLegalTraditional = 34
    TaiwaneseCountingThousand = 35
    TaiwaneseDigital = 36
    ChineseCounting = 37
    ChineseLegalSimplified = 38
    ChineseCountingThousand = 39
    Special = 58
    NumberInDash = 57
    none = 255
    CustomType = 65280

