from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CalendarType(Enum):
    """
    Enum class representing different calendar types.
    """
    Default = 0
    Gregorian = 0
    GregorianArabic = 1
    GregorianMiddleEastFrench = 2
    GregorianEnglish = 3
    GregorianTransliteratedEnglish = 4
    GregorianTransliteratedFrench = 5
    Hebrew = 6
    Hijri = 7
    Japan = 8
    Korean = 9
    none = 10
    Saka = 11
    Taiwan = 12
    Thai = 13
