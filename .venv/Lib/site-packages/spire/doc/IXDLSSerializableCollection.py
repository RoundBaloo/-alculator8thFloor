from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IXDLSSerializableCollection (  IEnumerable) :
    """
    This class represents a collection that can be serialized/deserialized.

    Attributes:
    - TagItemName: The name of the tag for each item in the collection.
    - Count: The number of items in the collection.
    """

    @abc.abstractmethod
    def AddNewItem(self ,reader:'IXDLSContentReader')->'IDocumentSerializable':
        """
        Adds a new item to the collection based on the provided reader.

        Args:
        - reader: The reader used to deserialize the item.

        Returns:
        - The deserialized item.
        """
        pass



    @abc.abstractmethod
    def CreateNewItem(self ,reader:'IXDLSContentReader')->'IDocumentSerializable':
        """
        Creates a new item for the collection based on the provided reader.

        Args:
        - reader: The reader used to deserialize the item.

        Returns:
        - The created item.
        """
        pass



    @abc.abstractmethod
    def AddItem(self ,item:'IDocumentSerializable'):
        """
        Adds an item to the collection.

        Args:
        - item: The item to be added.
        """
        pass


    @property

    @abc.abstractmethod
    def TagItemName(self)->str:
        """
        Gets the name of the tag for each item in the collection.

        Returns:
        - The tag item name.
        """
        pass


    @property
    @abc.abstractmethod
    def Count(self)->int:
        """
        Gets the number of items in the collection.

        Returns:
        - The count of items.
        """
        pass


