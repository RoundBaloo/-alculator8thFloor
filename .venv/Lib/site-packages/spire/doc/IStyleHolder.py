from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IStyleHolder (abc.ABC) :
    """
    An abstract base class for objects that can hold a style.

    Attributes:
    - StyleName: The name of the style.

    Methods:
    - ApplyStyle(styleName: str): Applies a style with the given name.
    - ApplyStyle(builtinStyle: BuiltinStyle): Applies a built-in style.
    """
    @property

    @abc.abstractmethod
    def StyleName(self)->str:
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def ApplyStyle(self ,styleName:str):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def ApplyStyle(self ,builtinStyle:BuiltinStyle):
        """

        """
        pass


