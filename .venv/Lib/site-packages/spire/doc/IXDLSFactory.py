from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IXDLSFactory (abc.ABC) :
    """
    Abstract base class for XDLS factory.

    Methods:
    - Create: Create an instance of IDocumentSerializable.

    """

    @abc.abstractmethod
    def Create(self ,reader:'IXDLSContentReader')->'IDocumentSerializable':
        """
        Create an instance of IDocumentSerializable.

        Parameters:
        - reader: An instance of IXDLSContentReader.

        Returns:
        - An instance of IDocumentSerializable.

        """
        pass


