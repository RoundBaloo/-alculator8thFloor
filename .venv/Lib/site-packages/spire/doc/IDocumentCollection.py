from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IDocumentCollection(ICollectionBase, IEnumerable):
    """
    Represents a collection of documents.
    """

    @abc.abstractmethod
    def get_Item(self, index: int) -> 'IDocument':
        """
        Retrieves the document at the specified index.

        Parameters:
        - index (int): The index of the document to retrieve.

        Returns:
        - IDocument: The document at the specified index.
        """
        pass
