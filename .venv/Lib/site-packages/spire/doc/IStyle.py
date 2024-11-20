from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IStyle (abc.ABC) :
    """
    Abstract base class for style objects.
    """
    @property

    @abc.abstractmethod
    def Name(self)->str:
        """
        Get the name of the style.
        """
        pass


    @Name.setter
    @abc.abstractmethod
    def Name(self, value:str):
        """
        Set the name of the style.
        """
        pass


    @property

    @abc.abstractmethod
    def StyleId(self)->str:
        """
        Get the ID of the style.
        """
        pass


    @property

    @abc.abstractmethod
    def GetStyleType(self)->'StyleType':
        """
        Get the type of the style.
        """
        pass



    @abc.abstractmethod
    def Clone(self)->'IStyle':
        """
        Create a clone of the style.
        """
        pass


