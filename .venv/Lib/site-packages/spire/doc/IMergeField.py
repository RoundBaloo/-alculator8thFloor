from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IMergeField (  IField, ITextRange, IParagraphBase, IDocumentObject) :
    """
    Represents a merge field in a document.
    """
    @property

    @abc.abstractmethod
    def FieldName(self)->str:
        """
        Gets or sets the name of the merge field.
        """
        pass


    @FieldName.setter
    @abc.abstractmethod
    def FieldName(self, value:str):
        """
        Sets the name of the merge field.
        """
        pass


    @property

    @abc.abstractmethod
    def TextBefore(self)->str:
        """
        Gets or sets the text before the merge field.
        """
        pass


    @TextBefore.setter
    @abc.abstractmethod
    def TextBefore(self, value:str):
        """
        Sets the text before the merge field.
        """
        pass


    @property

    @abc.abstractmethod
    def TextAfter(self)->str:
        """
        Gets or sets the text after the merge field.
        """
        pass


    @TextAfter.setter
    @abc.abstractmethod
    def TextAfter(self, value:str):
        """
        Sets the text after the merge field.
        """
        pass


