from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ParagraphCollection (  DocumentSubsetCollection, IParagraphCollection) :
    """
    Represents a collection of paragraphs in a document.
    """

    def get_Item(self ,index:int)->'Paragraph':
        """
        Gets the paragraph at the specified index.

        Args:
            index: The index of the paragraph.

        Returns:
            The paragraph at the specified index.
        """
        
        GetDllLibDoc().ParagraphCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ParagraphCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ParagraphCollection_get_Item,self.Ptr, index)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret



    def Add(self ,paragraph:'IParagraph')->int:
        """
        Adds a paragraph to the end of the collection.

        Args:
            paragraph: The paragraph to add.

        Returns:
            The index at which the paragraph was added.
        """
        intPtrparagraph:c_void_p = paragraph.Ptr

        GetDllLibDoc().ParagraphCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ParagraphCollection_Add.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ParagraphCollection_Add,self.Ptr, intPtrparagraph)
        return ret


    def Contains(self ,paragraph:'IParagraph')->bool:
        """
        Determines whether the collection contains a specific paragraph.

        Args:
            paragraph: The paragraph to check.

        Returns:
            True if the paragraph is found in the collection, False otherwise.
        """
        intPtrparagraph:c_void_p = paragraph.Ptr

        GetDllLibDoc().ParagraphCollection_Contains.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ParagraphCollection_Contains.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().ParagraphCollection_Contains,self.Ptr, intPtrparagraph)
        return ret


    def Insert(self ,index:int,paragraph:'IParagraph'):
        """
        Inserts a paragraph into the collection at the specified index.

        Args:
            index: The index at which to insert the paragraph.
            paragraph: The paragraph to insert.
        """
        intPtrparagraph:c_void_p = paragraph.Ptr

        GetDllLibDoc().ParagraphCollection_Insert.argtypes=[c_void_p ,c_int,c_void_p]
        CallCFunction(GetDllLibDoc().ParagraphCollection_Insert,self.Ptr, index,intPtrparagraph)


    def IndexOf(self ,paragraph:'IParagraph')->int:
        """
        Returns the zero-based index of the specified paragraph.

        Args:
            paragraph: The paragraph to find.

        Returns:
            The index of the paragraph, or -1 if it is not found.
        """
        intPtrparagraph:c_void_p = paragraph.Ptr

        GetDllLibDoc().ParagraphCollection_IndexOf.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ParagraphCollection_IndexOf.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ParagraphCollection_IndexOf,self.Ptr, intPtrparagraph)
        return ret


    def Remove(self ,paragraph:'IParagraph'):
        """
        Removes the specified paragraph from the collection.

        Args:
            paragraph: The paragraph to remove.
        """
        intPtrparagraph:c_void_p = paragraph.Ptr

        GetDllLibDoc().ParagraphCollection_Remove.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().ParagraphCollection_Remove,self.Ptr, intPtrparagraph)


    def RemoveAt(self ,index:int):
        """
        Removes the paragraph at the specified index from the collection.

        Args:
            index: The index of the paragraph to remove.
        """
        
        GetDllLibDoc().ParagraphCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().ParagraphCollection_RemoveAt,self.Ptr, index)

