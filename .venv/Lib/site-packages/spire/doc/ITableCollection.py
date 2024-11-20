from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ITableCollection (  IDocumentObjectCollection, ICollectionBase, IEnumerable) :
    """
    Represents a collection of tables in a document.
    """

    @abc.abstractmethod
    def get_Item(self ,index:int)->'ITable':
        """
        Retrieves the table at the specified index.

        Args:
            index (int): The index of the table to retrieve.

        Returns:
            ITable: The table at the specified index.
        """
        pass



    @abc.abstractmethod
    def Add(self ,table:'ITable')->int:
        """
        Adds a table to the collection.

        Args:
            table (ITable): The table to add.

        Returns:
            int: The index at which the table was added.
        """
        pass



    @abc.abstractmethod
    def IndexOf(self ,table:'ITable')->int:
        """
        Retrieves the index of the specified table.

        Args:
            table (ITable): The table to find.

        Returns:
            int: The index of the table, or -1 if not found.
        """
        pass



    @abc.abstractmethod
    def Contains(self ,table:'ITable')->bool:
        """
        Checks if the collection contains the specified table.

        Args:
            table (ITable): The table to check.

        Returns:
            bool: True if the table is in the collection, False otherwise.
        """
        pass
