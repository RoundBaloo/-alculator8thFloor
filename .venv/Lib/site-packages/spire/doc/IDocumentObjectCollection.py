from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IDocumentObjectCollection (  ICollectionBase, IEnumerable) :
    """
    Represents a collection of document objects.
    """

    @abc.abstractmethod
    def get_Item(self ,index:int)->'DocumentObject':
        """
        Retrieves the document object at the specified index.

        Args:
            index (int): The index of the document object to retrieve.

        Returns:
            DocumentObject: The document object at the specified index.
        """
        pass


