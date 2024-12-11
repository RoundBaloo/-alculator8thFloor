from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IBody (  ICompositeObject, IDocumentObject) :
    """
    Interface for the body of a document.
    """
    @property

    @abc.abstractmethod
    def Tables(self)->'TableCollection':
        """
        Returns the collection of tables in the body.
        """
        pass


    @property

    @abc.abstractmethod
    def Paragraphs(self)->'ParagraphCollection':
        """
        Returns the collection of paragraphs in the body.
        """
        pass


    @property

    @abc.abstractmethod
    def FormFields(self)->'FormFieldCollection':
        """
        Returns the collection of form fields in the body.
        """
        pass


    @property

    @abc.abstractmethod
    def LastParagraph(self)->'IParagraph':
        """
        Returns the last paragraph in the body.
        """
        pass



    @abc.abstractmethod
    def AddParagraph(self)->'Paragraph':
        """
        Adds a new paragraph to the body and returns it.
        """
        pass



    @abc.abstractmethod
    def AddTable(self)->'Table':
        """
        Adds a new table to the body and returns it.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def InsertXHTML(self ,html:str):
        """
        Inserts the given XHTML into the body.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def InsertXHTML(self ,html:str,paragraphIndex:int):
        """
        Inserts the given XHTML into the body at the specified paragraph index.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def InsertXHTML(self ,html:str,paragraphIndex:int,paragraphItemIndex:int):
        """
        Inserts the given XHTML into the body at the specified paragraph and item index.
        """
        pass


    @abc.abstractmethod
    def EnsureMinimum(self):
        """
        Ensures that the body has a minimum structure.
        """
        pass


