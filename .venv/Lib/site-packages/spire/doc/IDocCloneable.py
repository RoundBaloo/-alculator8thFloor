from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IDocCloneable (abc.ABC) :
    """
    An abstract base class for objects that can be cloned.
    """

    @abc.abstractmethod
    def Clone(self)->'SpireObject':
        """
        Clone the object and return a new instance of the same type.
        """
        pass


