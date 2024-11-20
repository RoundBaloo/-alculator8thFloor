from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FootnoteRestartRule(Enum):
    """
    Specifies the restart rule for footnotes.
    
    """
    DoNotRestart = 0
    RestartSection = 1
    RestartPage = 2
    Default = 0
