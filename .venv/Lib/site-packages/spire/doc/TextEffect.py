from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextEffect(Enum):
    """
    Animation effect for text.
    """
    none = 0
    LasVegasLights = 1
    BlinkingBackground = 2
    SparkleText = 3
    MarchingBlackAnts = 4
    MarchingRedAnts = 5
    Shimmer = 6
