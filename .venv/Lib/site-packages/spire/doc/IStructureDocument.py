from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IStructureDocument (  ICompositeObject, IDocumentObject) :
    """
    Represents a structure document.
    """
    @property

    @abc.abstractmethod
    def SDTProperties(self)->'SDTProperties':
        """
        Get the Sdt properties.
        """
        pass


    @property

    @abc.abstractmethod
    def BreakCharacterFormat(self)->'CharacterFormat':
        """
        Get the character format of the break.
        """
        pass


    @abc.abstractmethod
    def UpdateDataBinding(self):
        """
        Updates structured document tag content with bound data.
        """
        pass


