from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IDocumentSerializable(abc.ABC):
    """
    An abstract base class for document serializable objects.
    """

    @abc.abstractmethod
    def WriteXmlAttributes(self ,writer:'IXDLSAttributeWriter'):
        """
        Writes the XML attributes of the object.

        Args:
            writer: The writer object used to write the XML attributes.
        """
        pass



    @abc.abstractmethod
    def WriteXmlContent(self ,writer:'IXDLSContentWriter'):
        """
        Writes the XML content of the object.

        Args:
            writer: The writer object used to write the XML content.
        """
        pass



    @abc.abstractmethod
    def ReadXmlAttributes(self ,reader:'IXDLSAttributeReader'):
        """
        Reads the XML attributes of the object.

        Args:
            reader: The reader object used to read the XML attributes.
        """
        pass



    @abc.abstractmethod
    def ReadXmlContent(self ,reader:'IXDLSContentReader')->bool:
        """
        Reads the XML content of the object.

        Args:
            reader: The reader object used to read the XML content.

        Returns:
            bool: True if the XML content was successfully read, False otherwise.
        """
        pass


    @property

    @abc.abstractmethod
    def XDLSHolder(self)->'XDLSHolder':
        """
        Gets the XDLSHolder object associated with the object.

        Returns:
            XDLSHolder: The XDLSHolder object associated with the object.
        """
        pass



    @abc.abstractmethod
    def RestoreReference(self ,name:str,value:int):
        """
        Restores a reference to an object.

        Args:
            name: The name of the reference.
            value: The value of the reference.
        """
        pass


