from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ITextBoxItemCollection (abc.ABC) :
    """
    Interface for a collection of text box items.
    """

    @abc.abstractmethod
    def get_Item(self ,index:int)->'ITextBox':
        """
        Get the text box item at the specified index.

        Args:
            index: The index of the text box item.

        Returns:
            The text box item at the specified index.
        """
        pass



    @abc.abstractmethod
    def Add(self ,textBox:'ITextBox')->int:
        """
        Add a text box item to the collection.

        Args:
            textBox: The text box item to add.

        Returns:
            The index at which the text box item was added.
        """
        pass


