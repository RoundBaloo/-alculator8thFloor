from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SummaryDocumentProperties (  DocumentSerializable) :
    """
    Represents the summary document properties.
    """
    @property

    def Author(self)->str:
        """
        Gets or sets the author name.
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Author.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Author.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_Author,self.Ptr))
        return ret


    @Author.setter
    def Author(self, value:str):
        """
        Sets the author name.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Author.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_Author,self.Ptr, valuePtr)

    @property

    def ApplicationName(self)->str:
        """
        Gets or sets the application name.
        """
        GetDllLibDoc().SummaryDocumentProperties_get_ApplicationName.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_ApplicationName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_ApplicationName,self.Ptr))
        return ret


    @ApplicationName.setter
    def ApplicationName(self, value:str):
        """
        Sets the application name.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_ApplicationName.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_ApplicationName,self.Ptr, valuePtr)

    @property

    def Title(self)->str:
        """
        Gets or sets the document title.
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Title.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Title.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_Title,self.Ptr))
        return ret


    @Title.setter
    def Title(self, value:str):
        """
        Sets the document title.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Title.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_Title,self.Ptr, valuePtr)

    @property

    def Subject(self)->str:
        """
        Gets or sets the subject of the document.
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Subject.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Subject.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_Subject,self.Ptr))
        return ret


    @Subject.setter
    def Subject(self, value:str):
        """
        Sets the subject of the document.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Subject.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_Subject,self.Ptr, valuePtr)

    @property

    def Keywords(self)->str:
        """
        Gets or sets the document keywords.
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Keywords.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Keywords.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_Keywords,self.Ptr))
        return ret


    @Keywords.setter
    def Keywords(self, value:str):
        """
        Sets the document keywords.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Keywords.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_Keywords,self.Ptr, valuePtr)

    @property

    def Comments(self)->str:
        """
        Gets or sets the comments that provide additional information about the document.
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Comments.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Comments.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_Comments,self.Ptr))
        return ret


    @Comments.setter
    def Comments(self, value:str):
        """
        Sets the comments that provide additional information about the document.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Comments.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_Comments,self.Ptr, valuePtr)

    @property

    def Template(self)->str:
        """
        Gets or sets the template name of the document.
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Template.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Template.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_Template,self.Ptr))
        return ret


    @Template.setter
    def Template(self, value:str):
        """
        Sets the template name of the document.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Template.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_Template,self.Ptr, valuePtr)

    @property

    def LastAuthor(self)->str:
        """
        Gets or sets the last author name.
        """
        GetDllLibDoc().SummaryDocumentProperties_get_LastAuthor.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_LastAuthor.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_LastAuthor,self.Ptr))
        return ret


    @LastAuthor.setter
    def LastAuthor(self, value:str):
        """
        Sets the last author name.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_LastAuthor.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_LastAuthor,self.Ptr, valuePtr)

    @property

    def RevisionNumber(self)->str:
        """
        Gets or sets the document revision number.
        """
        GetDllLibDoc().SummaryDocumentProperties_get_RevisionNumber.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_RevisionNumber.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_RevisionNumber,self.Ptr))
        return ret


    @RevisionNumber.setter
    def RevisionNumber(self, value:str):
        """
        Sets the document revision number.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_RevisionNumber.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_RevisionNumber,self.Ptr, valuePtr)

    @property

    def TotalEditingTime(self)->'TimeSpan':
        """
        Gets or sets the document total editing time
        """
        GetDllLibDoc().SummaryDocumentProperties_get_TotalEditingTime.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_TotalEditingTime.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_TotalEditingTime,self.Ptr)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @TotalEditingTime.setter
    def TotalEditingTime(self, value:'TimeSpan'):
        """
        Gets or sets the document total editing time.
        """
        GetDllLibDoc().SummaryDocumentProperties_set_TotalEditingTime.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_TotalEditingTime,self.Ptr, value.Ptr)

    @property

    def LastPrinted(self)->'DateTime':
        """
        Returns or sets the last print date
        """
        GetDllLibDoc().SummaryDocumentProperties_get_LastPrinted.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_LastPrinted.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_LastPrinted,self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @LastPrinted.setter
    def LastPrinted(self, value:'DateTime'):
        GetDllLibDoc().SummaryDocumentProperties_set_LastPrinted.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_LastPrinted,self.Ptr, value.Ptr)

    @property

    def CreateDate(self)->'DateTime':
        """
        Gets or sets the document creation date
        """
        GetDllLibDoc().SummaryDocumentProperties_get_CreateDate.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_CreateDate.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_CreateDate,self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @CreateDate.setter
    def CreateDate(self, value:'DateTime'):
        GetDllLibDoc().SummaryDocumentProperties_set_CreateDate.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_CreateDate,self.Ptr, value.Ptr)

    @property

    def LastSaveDate(self)->'DateTime':
        """
        Returns or sets the last save date
        """
        GetDllLibDoc().SummaryDocumentProperties_get_LastSaveDate.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_LastSaveDate.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_LastSaveDate,self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @LastSaveDate.setter
    def LastSaveDate(self, value:'DateTime'):
        GetDllLibDoc().SummaryDocumentProperties_set_LastSaveDate.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_LastSaveDate,self.Ptr, value.Ptr)

    @property
    def PageCount(self)->int:
        """
        Gets document pages count
        """
        GetDllLibDoc().SummaryDocumentProperties_get_PageCount.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_PageCount.restype=c_int
        ret = CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_PageCount,self.Ptr)
        return ret

    @property
    def WordCount(self)->int:
        """
        Gets document words count
        """
        GetDllLibDoc().SummaryDocumentProperties_get_WordCount.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_WordCount.restype=c_int
        ret = CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_WordCount,self.Ptr)
        return ret

    @property
    def CharCount(self)->int:
        """
        Gets document characters count
        """
        GetDllLibDoc().SummaryDocumentProperties_get_CharCount.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_CharCount.restype=c_int
        ret = CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_CharCount,self.Ptr)
        return ret

    @property
    def CharCountWithSpace(self)->int:
        """
        Gets document characters count(including spaces)
        """
        GetDllLibDoc().SummaryDocumentProperties_get_CharCountWithSpace.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_CharCountWithSpace.restype=c_int
        ret = CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_CharCountWithSpace,self.Ptr)
        return ret

    @property

    def Thumbnail(self)->str:
        """
        Returns or setsthumbnail picture for document preview
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Thumbnail.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Thumbnail.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_Thumbnail,self.Ptr))
        return ret


    @Thumbnail.setter
    def Thumbnail(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().SummaryDocumentProperties_set_Thumbnail.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_Thumbnail,self.Ptr, valuePtr)

    @property
    def DocSecurity(self)->int:
        """
        Gets or sets document security level
        """
        GetDllLibDoc().SummaryDocumentProperties_get_DocSecurity.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_DocSecurity.restype=c_int
        ret = CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_DocSecurity,self.Ptr)
        return ret

    @DocSecurity.setter
    def DocSecurity(self, value:int):
        GetDllLibDoc().SummaryDocumentProperties_set_DocSecurity.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_set_DocSecurity,self.Ptr, value)

    @property
    def Count(self)->int:
        """
        Gets summary count of document properties
        """
        GetDllLibDoc().SummaryDocumentProperties_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().SummaryDocumentProperties_get_Count.restype=c_int
        ret = CallCFunction(GetDllLibDoc().SummaryDocumentProperties_get_Count,self.Ptr)
        return ret


    def Add(self ,key:int,props:'DocumentProperty'):
        """
        Adds the specified documentProperty.

        Args:
            key (int): The key to insert.
            props (DocumentProperty): The documentProperty to insert.
        """
        intPtrprops:c_void_p = props.Ptr

        GetDllLibDoc().SummaryDocumentProperties_Add.argtypes=[c_void_p ,c_int,c_void_p]
        CallCFunction(GetDllLibDoc().SummaryDocumentProperties_Add,self.Ptr, key,intPtrprops)

