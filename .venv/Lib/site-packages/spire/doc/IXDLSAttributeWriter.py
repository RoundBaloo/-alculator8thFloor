from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IXDLSAttributeWriter (abc.ABC) :
    """
    Abstract base class for writing attribute values.
    """
    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:float):
        """
        Abstract method for writing a float value.

        Args:
            name (str): The name of the attribute.
            value (float): The float value to write.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:int):
        """
        Abstract method for writing an integer value.

        Args:
            name (str): The name of the attribute.
            value (int): The integer value to write.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:str):
        """
        Abstract method for writing a string value.

        Args:
            name (str): The name of the attribute.
            value (str): The string value to write.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:Enum):
        """
        Abstract method for writing an enum value.

        Args:
            name (str): The name of the attribute.
            value (Enum): The enum value to write.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:bool):
        """
        Abstract method for writing a boolean value.

        Args:
            name (str): The name of the attribute.
            value (bool): The boolean value to write.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:Color):
        """
        Abstract method for writing a color value.

        Args:
            name (str): The name of the attribute.
            value (Color): The color value to write.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def WriteValue(self ,name:str,value:DateTime):
        """
        Abstract method for writing a datetime value.

        Args:
            name (str): The name of the attribute.
            value (DateTime): The datetime value to write.
        """
        pass


