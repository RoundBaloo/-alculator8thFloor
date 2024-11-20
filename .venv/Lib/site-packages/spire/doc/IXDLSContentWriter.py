from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IXDLSContentWriter (abc.ABC) :
    """
    Abstract base class for XDLS content writers.
    """
#
#    @abc.abstractmethod
#    def WriteChildBinaryElement(self ,name:str,value:'Byte[]'):
#        """
#
#        """
#        pass
#



    @abc.abstractmethod
    def WriteChildStringElement(self ,name:str,value:str):
        """
        Writes a child string element.

        Args:
            name (str): The name of the element.
            value (str): The value of the element.
        """
        pass



    @abc.abstractmethod
    def WriteChildElement(self ,name:str,value:'SpireObject'):
        """
        Writes a child element.

        Args:
            name (str): The name of the element.
            value (SpireObject): The value of the element.
        """
        pass



    @abc.abstractmethod
    def WriteChildRefElement(self ,name:str,refToElement:int):
        """
        Writes a child reference element.

        Args:
            name (str): The name of the element.
            refToElement (int): The reference to the element.
        """
        pass


#    @property
#
#    @abc.abstractmethod
#    def InnerWriter(self)->'XmlWriter':
#        """
#
#        """
#        pass
#


