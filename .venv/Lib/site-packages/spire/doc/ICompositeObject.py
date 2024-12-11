from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ICompositeObject (  IDocumentObject) :
    """
    Represents a composite object in a document.

    Attributes:
        ChildObjects (DocumentObjectCollection): The collection of child objects.
    """
    @property

    @abc.abstractmethod
    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the collection of child objects.

        Returns:
            DocumentObjectCollection: The collection of child objects.
        """
        pass


