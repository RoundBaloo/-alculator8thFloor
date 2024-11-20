from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Comment(ParagraphBase, ICompositeObject):
    """
    Represents a container for text of a comment.
    """
    @dispatch
    def __init__(self, doc:IDocument):
        """
        Initializes a new instance of the Comment class.
        :param doc: The document.
        """
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().Comment_CreateCommentD.argtypes=[c_void_p]
        GetDllLibDoc().Comment_CreateCommentD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Comment_CreateCommentD,intPdoc)
        super(Comment, self).__init__(intPtr)

    @property
    def ChildObjects(self) -> 'DocumentObjectCollection':
        """
        Gets the child document objects.
        :return: The child entities.
        """
        GetDllLibDoc().Comment_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Comment_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret

    @property
    def DocumentObjectType(self) -> 'DocumentObjectType':
        """
        Gets the type of the document object.
        :return: The type of the document object.
        """
        GetDllLibDoc().Comment_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Comment_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def Body(self) -> 'Body':
        """
        Gets comment body.
        :return: The text body.
        """
        GetDllLibDoc().Comment_get_Body.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_Body.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Comment_get_Body,self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret

    @property
    def Format(self) -> 'CommentFormat':
        """
        Gets the format.
        :return: The format.
        """
        GetDllLibDoc().Comment_get_Format.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_Format.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Comment_get_Format,self.Ptr)
        from spire.doc import CommentFormat
        ret = None if intPtr==None else CommentFormat(intPtr)
        return ret

    @property
    def Items(self) -> 'ParagraphItemCollection':
        """
        Gets the range of commented items.
        :return: The range comment contains.
        """
        GetDllLibDoc().Comment_get_Items.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_Items.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Comment_get_Items,self.Ptr)
        ret = None if intPtr==None else ParagraphItemCollection(intPtr)
        return ret

    @property
    def ReplyCommentItems(self) -> 'CommentsCollection':
        """
        Gets the range of commented items.
        :return: The reply commented range.
        """
        GetDllLibDoc().Comment_get_ReplyCommentItems.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_ReplyCommentItems.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Comment_get_ReplyCommentItems,self.Ptr)
        ret = None if intPtr==None else CommentsCollection(intPtr)
        return ret

    @property
    def ByRepliedComment(self) -> 'Comment':
        """
        Gets the comment of current comment replied.
        :return: Comment of by reply.
        """
        GetDllLibDoc().Comment_get_ByRepliedComment.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_ByRepliedComment.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Comment_get_ByRepliedComment,self.Ptr)
        ret = None if intPtr==None else Comment(intPtr)
        return ret

    @property
    def MarkDone(self) -> bool:
        """
        Gets a value indicating whether done.
        :return: True if done, False otherwise.
        """
        GetDllLibDoc().Comment_get_MarkDone.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_MarkDone.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Comment_get_MarkDone,self.Ptr)
        return ret

    @property
    def CommentMarkStart(self) -> 'CommentMark':
        """
        Gets the beginning mark of the comment.
        :return: The commentMark of start.
        """
        GetDllLibDoc().Comment_get_CommentMarkStart.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_CommentMarkStart.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Comment_get_CommentMarkStart,self.Ptr)
        ret = None if intPtr==None else CommentMark(intPtr)
        return ret


    @property
    def CommentMarkEnd(self) -> 'CommentMark':
        """
        Gets the ending mark of the comment.
        :return: The commentMark of end.
        """
        GetDllLibDoc().Comment_get_CommentMarkEnd.argtypes=[c_void_p]
        GetDllLibDoc().Comment_get_CommentMarkEnd.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Comment_get_CommentMarkEnd,self.Ptr)
        ret = None if intPtr==None else CommentMark(intPtr)
        return ret

    def Clear(self):
        """
        Clears the commented items.
        """
        GetDllLibDoc().Comment_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Comment_Clear,self.Ptr)

    @dispatch

    def Replace(self ,text:str):
        """
        Replace commented items with matchString text.
        :param text: The text.
        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().Comment_Replace.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Comment_Replace,self.Ptr, textPtr)

    @dispatch
    def Replace(self, textBodyPart: TextBodyPart):
        """
        Replaces the commented items with specified TextBodyPart.
        :param textBodyPart: The text body part.
        """
        intPtrtextBodyPart:c_void_p = textBodyPart.Ptr

        GetDllLibDoc().Comment_ReplaceT.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Comment_ReplaceT,self.Ptr, intPtrtextBodyPart)


    def AddItem(self ,paraItem:'IParagraphBase'):
        """
        Adds the paragraph item to the commented items.
        :param paraItem: The paragraph item.
        :returns: None
        """
        intPtrparaItem:c_void_p = paraItem.Ptr

        GetDllLibDoc().Comment_AddItem.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Comment_AddItem,self.Ptr, intPtrparaItem)


    def ReplyToComment(self ,replyComment:'Comment'):
        """
        Replies to comment.
        :param replyComment: The reply comment.
        :returns: None
        """
        intPtrreplyComment:c_void_p = replyComment.Ptr

        GetDllLibDoc().Comment_ReplyToComment.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Comment_ReplyToComment,self.Ptr, intPtrreplyComment)


    def MarkCommentDone(self ,done:bool):
        """
        Marks the comment done.
        :param done: The done.
        :returns: None
        """
        
        GetDllLibDoc().Comment_MarkCommentDone.argtypes=[c_void_p ,c_bool]
        CallCFunction(GetDllLibDoc().Comment_MarkCommentDone,self.Ptr, done)

    def EnsureMinimum(self):
        """
        Ensures the minimum.
        :returns: None
        """
        GetDllLibDoc().Comment_EnsureMinimum.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Comment_EnsureMinimum,self.Ptr)

