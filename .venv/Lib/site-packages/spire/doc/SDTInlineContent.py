from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SDTInlineContent (  DocumentBase, ICompositeObject) :
    """
    This element specifies the last known contents of a structured document tag around one or more inline-level structures.
    """
    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the child objects.
        """
        GetDllLibDoc().SDTInlineContent_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().SDTInlineContent_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SDTInlineContent_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the entity.
        """
        GetDllLibDoc().SDTInlineContent_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().SDTInlineContent_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().SDTInlineContent_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def OwnerParagraph(self)->'Paragraph':
        """
        Gets the object owner paragraph.
        """
        GetDllLibDoc().SDTInlineContent_get_OwnerParagraph.argtypes=[c_void_p]
        GetDllLibDoc().SDTInlineContent_get_OwnerParagraph.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SDTInlineContent_get_OwnerParagraph,self.Ptr)
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @property

    def Text(self)->str:
        """
        Returns or sets STD text.
        """
        GetDllLibDoc().SDTInlineContent_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().SDTInlineContent_get_Text.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SDTInlineContent_get_Text,self.Ptr))
        return ret



    def get_Item(self ,index:int)->'ParagraphBase':
        """
        Gets paragraph item by index.
        """
        
        GetDllLibDoc().SDTInlineContent_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().SDTInlineContent_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SDTInlineContent_get_Item,self.Ptr, index)
        ret = None if intPtr==None else ParagraphBase(intPtr)
        return ret


