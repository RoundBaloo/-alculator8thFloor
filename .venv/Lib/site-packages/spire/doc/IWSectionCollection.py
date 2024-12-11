from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IWSectionCollection (  IDocumentObjectCollection, ICollectionBase, IEnumerable) :
    """
    This class represents a collection of sections in a document.

    Attributes:
        None

    Methods:
        get_Item(index: int) -> Section: Returns the section at the specified index.
        Add(section: ISection) -> int: Adds a section to the collection and returns the index of the added section.
        IndexOf(section: ISection) -> int: Returns the index of the specified section in the collection.
    """

    @abc.abstractmethod
    def get_Item(self ,index:int)->'Section':
        """
        Returns the section at the specified index.

        Args:
            index (int): The index of the section to retrieve.

        Returns:
            Section: The section at the specified index.
        """
        pass



    @abc.abstractmethod
    def Add(self ,section:'ISection')->int:
        """
        Adds a section to the collection and returns the index of the added section.

        Args:
            section (ISection): The section to add to the collection.

        Returns:
            int: The index of the added section.
        """
        pass



    @abc.abstractmethod
    def IndexOf(self ,section:'ISection')->int:
        """
        Returns the index of the specified section in the collection.

        Args:
            section (ISection): The section to find the index of.

        Returns:
            int: The index of the specified section.
        """
        pass


