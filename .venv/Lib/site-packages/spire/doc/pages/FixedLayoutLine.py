from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc import *
from ctypes import *
import abc

class FixedLayoutLine (  LayoutElement) :
    @dispatch
    def __init__(self):
        print('.')
    """
    <summary>
        Represents line of characters of text and inline objects.
    </summary>
    """
    @property

    def Text(self)->str:
        """
    <summary>
        Exports the contents of the entity into a string in plain text format.
    </summary>
        """
        GetDllLibDoc().FixedLayoutLine_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutLine_get_Text.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().FixedLayoutLine_get_Text,self.Ptr))
        return ret


    @property

    def Paragraph(self)->'Paragraph':
        """
    <summary>
        Returns the paragraph that corresponds to the layout entity.  
    </summary>
        """
        GetDllLibDoc().FixedLayoutLine_get_Paragraph.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutLine_get_Paragraph.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutLine_get_Paragraph,self.Ptr)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @property

    def Spans(self)->'LayoutFixedLSpanCollection':
        """
    <summary>
        Provides access to the spans of the line.
    </summary>
        """
        GetDllLibDoc().FixedLayoutLine_get_Spans.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutLine_get_Spans.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutLine_get_Spans,self.Ptr)
        ret = None if intPtr==None else LayoutFixedLSpanCollection(intPtr)
        return ret



