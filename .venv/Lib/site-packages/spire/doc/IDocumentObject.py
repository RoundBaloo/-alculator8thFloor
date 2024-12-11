from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IDocumentObject (abc.ABC) :
    """
    Abstract base class for document objects.
    """
    @property

    @abc.abstractmethod
    def Document(self)->'Document':
        """
        Returns the document that the object belongs to.
        """
        pass


    @property

    @abc.abstractmethod
    def Owner(self)->'DocumentObject':
        """
        Returns the owner of the object.
        """
        pass


    @property

    @abc.abstractmethod
    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Returns the type of the document object.
        """
        pass


    @property

    @abc.abstractmethod
    def NextSibling(self)->'IDocumentObject':
        """
        Returns the next sibling of the object.
        """
        pass


    @property

    @abc.abstractmethod
    def PreviousSibling(self)->'IDocumentObject':
        """
        Returns the previous sibling of the object.
        """
        pass


    @property
    @abc.abstractmethod
    def IsComposite(self)->bool:
        """
        Returns True if the object is composite, False otherwise.
        """
        pass



    @abc.abstractmethod
    def Clone(self)->'DocumentObject':
        """
        Creates a clone of the object.
        """
        pass



    @abc.abstractmethod
    def GetNextWidgetSibling(self)->'IDocumentObject':
        """
        Returns the next widget sibling of the object.
        """
        pass



    @abc.abstractmethod
    def GetPreviousWidgetSibling(self)->'IDocumentObject':
        """
        Returns the previous widget sibling of the object.
        """
        pass


