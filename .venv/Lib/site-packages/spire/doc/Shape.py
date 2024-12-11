from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Shape (  ShapeBase, IDocumentObject) :
    """
    Represents a shape in a document.
    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the document object type of the shape.
        """
        GetDllLibDoc().Shape_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Shape_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Shape_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def HasImage(self)->bool:
        """
        Returns True if the shape has an image.
        """
        GetDllLibDoc().Shape_get_HasImage.argtypes=[c_void_p]
        GetDllLibDoc().Shape_get_HasImage.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Shape_get_HasImage,self.Ptr)
        return ret

    @property

    def FirstParagraph(self)->'Paragraph':
        """
        Gets the first paragraph in the shape.
        """
        GetDllLibDoc().Shape_get_FirstParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Shape_get_FirstParagraph.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Shape_get_FirstParagraph,self.Ptr)
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @property

    def LastParagraph(self)->'Paragraph':
        """
        Gets the last paragraph in the shape.
        """
        GetDllLibDoc().Shape_get_LastParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Shape_get_LastParagraph.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Shape_get_LastParagraph,self.Ptr)
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @property
    def HasChart(self)->bool:
        """
        Returns True if the shape has a chart.
        """
        GetDllLibDoc().Shape_get_HasChart.argtypes=[c_void_p]
        GetDllLibDoc().Shape_get_HasChart.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Shape_get_HasChart,self.Ptr)
        return ret

