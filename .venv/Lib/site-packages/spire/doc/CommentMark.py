from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CommentMark(ParagraphBase, IDocumentObject):
    """
    Represents a container for text of a comment.
    """
    
    @dispatch
    def __init__(self, doc:IDocument):
        """
        Initializes a new instance of the CommentMark class with the specified document.
        """
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().CommentMark_CreateCommentMarkD.argtypes=[c_void_p]
        GetDllLibDoc().CommentMark_CreateCommentMarkD.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CommentMark_CreateCommentMarkD,intPdoc)
        super(CommentMark, self).__init__(intPtr)

    @dispatch
    def __init__(self, doc:IDocument, commentMarkType:CommentMarkType):
        """
        Initializes a new instance of the CommentMark class with the specified document and comment mark type.
        """
        intPdoc:c_void_p =  doc.Ptr
        iTypetype:c_int = commentMarkType.value

        GetDllLibDoc().CommentMark_CreateCommentMarkDT.argtypes=[c_void_p,c_int]
        GetDllLibDoc().CommentMark_CreateCommentMarkDT.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CommentMark_CreateCommentMarkDT,intPdoc,iTypetype)
        super(CommentMark, self).__init__(intPtr)

		

    @property
    def CommentId(self)->int:
        """
        Gets or sets the id of the comment this mark refers to.
        """
        GetDllLibDoc().CommentMark_get_CommentId.argtypes=[c_void_p]
        GetDllLibDoc().CommentMark_get_CommentId.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CommentMark_get_CommentId,self.Ptr)
        return ret

    @CommentId.setter
    def CommentId(self, value:int):
        """
        Sets the id of the comment this mark refers to.
        """
        GetDllLibDoc().CommentMark_set_CommentId.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().CommentMark_set_CommentId,self.Ptr, value)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.
        """
        GetDllLibDoc().CommentMark_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().CommentMark_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CommentMark_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Type(self)->'CommentMarkType':
        """
        Gets or sets the type of the CommentMark.
        """
        GetDllLibDoc().CommentMark_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().CommentMark_get_Type.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CommentMark_get_Type,self.Ptr)
        objwraped = CommentMarkType(ret)
        return objwraped

    @Type.setter
    def Type(self, value:'CommentMarkType'):
        """
        Sets the type of the CommentMark.
        """
        GetDllLibDoc().CommentMark_set_Type.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().CommentMark_set_Type,self.Ptr, value.value)

