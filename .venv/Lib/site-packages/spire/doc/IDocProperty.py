from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IDocProperty (abc.ABC) :
    """
    Abstract base class for document properties.
    """
    @property
    @abc.abstractmethod
    def IsBuiltIn(self)->bool:
        """
        Returns whether the property is built-in or not.
        """
        pass


    @property

    @abc.abstractmethod
    def PropertyId(self)->'BuiltInProperty':
        """
        Returns the ID of the property.
        """
        pass


    @property

    @abc.abstractmethod
    def Name(self)->str:
        """
        Returns the name of the property.
        """
        pass


    @property

    @abc.abstractmethod
    def Value(self)->'SpireObject':
        """
        Returns the value of the property.
        """
        pass


    @Value.setter
    @abc.abstractmethod
    def Value(self, value:'SpireObject'):
        """
        Sets the value of the property.
        """
        pass


    @property
    @abc.abstractmethod
    def Boolean(self)->bool:
        """
        Returns the boolean value of the property.
        """
        pass


    @Boolean.setter
    @abc.abstractmethod
    def Boolean(self, value:bool):
        """
        Sets the boolean value of the property.
        """
        pass


    @property
    @abc.abstractmethod
    def Integer(self)->int:
        """
        Returns the integer value of the property.
        """
        pass


    @Integer.setter
    @abc.abstractmethod
    def Integer(self, value:int):
        """
        Sets the integer value of the property.
        """
        pass


    @property
    @abc.abstractmethod
    def Int32(self)->int:
        """
        Returns the Int32 value of the property.
        """
        pass


    @Int32.setter
    @abc.abstractmethod
    def Int32(self, value:int):
        """
        Sets the Int32 value of the property.
        """
        pass


    @property
    @abc.abstractmethod
    def Double(self)->float:
        """
        Returns the double value of the property.
        """
        pass


    @Double.setter
    @abc.abstractmethod
    def Double(self, value:float):
        """
        Sets the double value of the property.
        """
        pass


    @property

    @abc.abstractmethod
    def Text(self)->str:
        """
        Returns the text value of the property.
        """
        pass


    @Text.setter
    @abc.abstractmethod
    def Text(self, value:str):
        """
        Sets the text value of the property.
        """
        pass


    @property

    @abc.abstractmethod
    def DateTime(self)->'DateTime':
        """
        Returns the DateTime value of the property.
        """
        pass


    @DateTime.setter
    @abc.abstractmethod
    def DateTime(self, value:'DateTime'):
        """
        Sets the DateTime value of the property.
        """
        pass


    @property

    @abc.abstractmethod
    def TimeSpan(self)->'TimeSpan':
        """
        Returns the TimeSpan value of the property.
        """
        pass


    @TimeSpan.setter
    @abc.abstractmethod
    def TimeSpan(self, value:'TimeSpan'):
        """
        Sets the TimeSpan value of the property.
        """
        pass


    @property

    @abc.abstractmethod
    def LinkSource(self)->str:
        """
        Returns the link source of the property.
        """
        pass


    @LinkSource.setter
    @abc.abstractmethod
    def LinkSource(self, value:str):
        """
        Sets the link source of the property.
        """
        pass


    @property
    @abc.abstractmethod
    def LinkToContent(self)->bool:
        """
        Returns whether the property is linked to content or not.
        """
        pass


    @LinkToContent.setter
    @abc.abstractmethod
    def LinkToContent(self, value:bool):
        """
        Sets whether the property is linked to content or not.
        """
        pass


