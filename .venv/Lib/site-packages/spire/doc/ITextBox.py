from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ITextBox (  IParagraphBase, ICompositeObject) :
    """
    Represents a text box in a document.
    """
    @property

    @abc.abstractmethod
    def Body(self)->'Body':
        """
        Gets the body of the text box.
        
        Returns:
            The body of the text box.
        """
        pass


    @property

    @abc.abstractmethod
    def Format(self)->'TextBoxFormat':
        """
        Gets the format of the text box.
        
        Returns:
            The format of the text box.
        """
        pass


