from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ITextRange (  IParagraphBase, IDocumentObject) :
    """
    Represents a range of text in a document.
    """
    @property

    @abc.abstractmethod
    def Text(self)->str:
        """
        Gets the text of the range.
        """
        pass


    @Text.setter
    @abc.abstractmethod
    def Text(self, value:str):
        """
        Sets the text of the range.
        """
        pass


    @property

    @abc.abstractmethod
    def CharacterFormat(self)->'CharacterFormat':
        """
        Gets the character format of the range.
        """
        pass



    @abc.abstractmethod
    def ApplyCharacterFormat(self ,charFormat:'CharacterFormat'):
        """
        Applies the specified character format to the range.
        """
        pass


