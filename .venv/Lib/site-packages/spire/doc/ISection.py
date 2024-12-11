from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ISection (  ICompositeObject, IDocumentObject) :
    """
    Represents a section in a document.
    """
    @property

    @abc.abstractmethod
    def Paragraphs(self)->'ParagraphCollection':
        """
        Gets the collection of paragraphs in the section.
        """
        pass


    @property

    @abc.abstractmethod
    def Tables(self)->'TableCollection':
        """
        Gets the collection of tables in the section.
        """
        pass


    @property

    @abc.abstractmethod
    def Body(self)->'Body':
        """
        Gets the body of the section.
        """
        pass


    @property

    @abc.abstractmethod
    def PageSetup(self)->'PageSetup':
        """
        Gets the page setup of the section.
        """
        pass


    @property

    @abc.abstractmethod
    def Columns(self)->'ColumnCollection':
        """
        Gets the collection of columns in the section.
        """
        pass


    @property

    @abc.abstractmethod
    def BreakCode(self)->'SectionBreakType':
        """
        Gets the section break code of the section.
        """
        pass


    @BreakCode.setter
    @abc.abstractmethod
    def BreakCode(self, value:'SectionBreakType'):
        """
        Sets the section break code of the section.
        """
        pass


    @property
    @abc.abstractmethod
    def ProtectForm(self)->bool:
        """
        Gets a value indicating whether the section is protected.
        """
        pass


    @ProtectForm.setter
    @abc.abstractmethod
    def ProtectForm(self, value:bool):
        """
        Sets a value indicating whether the section is protected.
        """
        pass



    @abc.abstractmethod
    def AddColumn(self ,width:float,spacing:float)->'Column':
        """
        Adds a column to the section with the specified width and spacing.
        """
        pass



    @abc.abstractmethod
    def AddParagraph(self)->'Paragraph':
        """
        Adds a paragraph to the section.
        """
        pass



    @abc.abstractmethod
    def AddTable(self)->'Table':
        """
        Adds a table to the section.
        """
        pass



    @abc.abstractmethod
    def Clone(self)->'Section':
        """
        Creates a deep copy of the section.
        """
        pass


    @abc.abstractmethod
    def MakeColumnsSameWidth(self):
        """
        Makes all columns in the section have the same width.
        """
        pass


    @property

    @abc.abstractmethod
    def HeadersFooters(self)->'HeadersFooters':
        """
        Gets the headers and footers of the section.
        """
        pass


