from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ICollectionBase (  IEnumerable) :
    """
    Base class for collection types.

    Attributes:
        Count (int): The number of items in the collection.
    """
    @property
    @abc.abstractmethod
    def Count(self)->int:
        """
        Returns the number of items in the collection.

        Returns:
            int: The number of items in the collection.
        """
        pass
