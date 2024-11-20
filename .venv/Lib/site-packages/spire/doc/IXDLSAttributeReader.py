from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IXDLSAttributeReader (abc.ABC) :
    """
    Abstract base class for attribute readers.
    """

    @abc.abstractmethod
    def HasAttribute(self ,name:str)->bool:
        """
        Check if an attribute with the given name exists.

        Args:
            name: The name of the attribute.

        Returns:
            True if the attribute exists, False otherwise.
        """
        pass



    @abc.abstractmethod
    def ReadString(self ,name:str)->str:
        """
        Read a string attribute with the given name.

        Args:
            name: The name of the attribute.

        Returns:
            The value of the attribute as a string.
        """
        pass



    @abc.abstractmethod
    def ReadInt(self ,name:str)->int:
        """
        Read an integer attribute with the given name.

        Args:
            name: The name of the attribute.

        Returns:
            The value of the attribute as an integer.
        """
        pass



    @abc.abstractmethod
    def ReadShort(self ,name:str)->'Int16':
        """
        Read a short attribute with the given name.

        Args:
            name: The name of the attribute.

        Returns:
            The value of the attribute as a short.
        """
        pass



    @abc.abstractmethod
    def ReadFloat(self ,name:str)->float:
        """
        Read a float attribute with the given name.

        Args:
            name: The name of the attribute.

        Returns:
            The value of the attribute as a float.
        """
        pass



    @abc.abstractmethod
    def ReadDouble(self ,name:str)->float:
        """
        Read a double attribute with the given name.

        Args:
            name: The name of the attribute.

        Returns:
            The value of the attribute as a double.
        """
        pass



    @abc.abstractmethod
    def ReadBoolean(self ,name:str)->bool:
        """
        Read a boolean attribute with the given name.

        Args:
            name: The name of the attribute.

        Returns:
            The value of the attribute as a boolean.
        """
        pass



    @abc.abstractmethod
    def ReadByte(self ,name:str)->int:
        """
        Read a byte attribute with the given name.

        Args:
            name: The name of the attribute.

        Returns:
            The value of the attribute as a byte.
        """
        pass


#
#    @abc.abstractmethod
#    def ReadEnum(self ,name:str,enumType:'Type')->'Enum':
#        """
#
#        """
#        pass
#



    @abc.abstractmethod
    def ReadColor(self ,name:str)->'Color':
        """
        Read a color attribute with the given name.

        Args:
            name: The name of the attribute.

        Returns:
            The value of the attribute as a color.
        """
        pass



    @abc.abstractmethod
    def ReadDateTime(self ,s:str)->'DateTime':
        """
        Read a datetime attribute with the given name.

        Args:
            s: The string representation of the datetime.

        Returns:
            The value of the attribute as a datetime.
        """
        pass


