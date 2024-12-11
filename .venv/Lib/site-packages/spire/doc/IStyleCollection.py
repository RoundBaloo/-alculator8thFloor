from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IStyleCollection (  ICollectionBase, IEnumerable) :
    """
    Represents a collection of styles.
    """

    @abc.abstractmethod
    def get_Item(self, index: int) -> 'IStyle':
        """
        Retrieves the style at the specified index.

        Args:
            index (int): The index of the style to retrieve.

        Returns:
            IStyle: The style at the specified index.
        """
        pass



    @abc.abstractmethod
    def Add(self ,style:'IStyle')->int:
        """
        Adds a style to the collection.

        Args:
            style (IStyle): The style to add.

        Returns:
            int: The index at which the style was added.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def FindByName(self ,name:str)->'Style':
        """
        Finds a style by its name.

        Args:
            name (str): The name of the style to find.

        Returns:
            Style: The found style.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def FindByName(self ,name:str,styleType:StyleType)->'IStyle':
        """
        Finds a style by its name and type.

        Args:
            name (str): The name of the style to find.
            styleType (StyleType): The type of the style to find.

        Returns:
            IStyle: The found style.
        """
        pass


