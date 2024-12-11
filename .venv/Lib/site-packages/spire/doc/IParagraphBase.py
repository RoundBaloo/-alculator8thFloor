from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IParagraphBase (  IDocumentObject) :
    """
    Represents a base interface for paragraphs in a document.
    """
    @property

    @abc.abstractmethod
    def OwnerParagraph(self)->'Paragraph':
        """
        Gets the owner paragraph of the current paragraph.
        """
        pass



    @abc.abstractmethod
    def ApplyStyle(self ,styleName:str):
        """
        Applies the character style to the paragraph.
        
        Args:
            styleName: The name of the style to apply.
        """
        pass


    @property

    @abc.abstractmethod
    def StyleName(self)->str:
        """
        Gets the style name of the paragraph.
        """
        pass


