from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IParagraphCollection (  IDocumentObjectCollection, ICollectionBase, IEnumerable) :
    """
    Represents a collection of paragraphs in a document.
    """

    @abc.abstractmethod
    def get_Item(self, index: int) -> 'Paragraph':
        """
        Gets the paragraph at the specified index.

        Args:
            index (int): The index of the paragraph.

        Returns:
            Paragraph: The paragraph at the specified index.
        """
        pass



    @abc.abstractmethod
    def Add(self ,paragraph:'IParagraph')->int:
        """
        Adds a paragraph to the collection.

        Args:
            paragraph (IParagraph): The paragraph to add.

        Returns:
            int: The index at which the paragraph was added.
        """
        pass



    @abc.abstractmethod
    def Insert(self ,index:int,paragraph:'IParagraph'):
        """
        Inserts a paragraph at the specified index.

        Args:
            index (int): The index at which to insert the paragraph.
            paragraph (IParagraph): The paragraph to insert.
        """
        pass



    @abc.abstractmethod
    def IndexOf(self ,paragraph:'IParagraph')->int:
        """
        Gets the index of the specified paragraph.

        Args:
            paragraph (IParagraph): The paragraph to find.

        Returns:
            int: The index of the specified paragraph.
        """
        pass



    @abc.abstractmethod
    def RemoveAt(self ,index:int):
        """
        Removes the paragraph at the specified index.

        Args:
            index (int): The index of the paragraph to remove.
        """
        pass
