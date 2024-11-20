from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IField (  ITextRange, IParagraphBase, IDocumentObject) :
    """
    Represents a field in a document.
    """
    @property

    @abc.abstractmethod
    def Type(self)->'FieldType':
        """
        Gets the type of the field.
        """
        pass


    @Type.setter
    @abc.abstractmethod
    def Type(self, value:'FieldType'):
        """
        Sets the type of the field.
        """
        pass


