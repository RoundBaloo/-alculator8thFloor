from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CharacterSpacing(Enum):
    """
    Enum for controlling character spacing.

    """
    doNotCompress = 0
    compressPunctuation = 1
    compressPunctuationAndJapaneseKana = 2
