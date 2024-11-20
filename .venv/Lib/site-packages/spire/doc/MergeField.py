from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MergeField (  Field, IMergeField) :
    """
    Represents a merge field in a document.
    """
    @dispatch
    def __init__(self, doc:IDocument):
        """
        Initializes a new instance of the MergeField class.

        Args:
            doc: The document to which the merge field belongs.
        """
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().MergeField_CreateMergeFieldD.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_CreateMergeFieldD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().MergeField_CreateMergeFieldD,intPdoc)
        super(MergeField, self).__init__(intPtr)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.

        Returns:
            The type of the document object.
        """
        GetDllLibDoc().MergeField_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().MergeField_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def FieldName(self)->str:
        """
        Returns or sets the field name.

        Returns:
            The field name.
        """
        GetDllLibDoc().MergeField_get_FieldName.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_FieldName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().MergeField_get_FieldName,self.Ptr))
        return ret


    @FieldName.setter
    def FieldName(self, value:str):
        """
        Sets the field name.

        Args:
            value: The field name to set.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().MergeField_set_FieldName.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().MergeField_set_FieldName,self.Ptr, valuePtr)

    @property

    def Text(self)->str:
        """
        Gets the text of the merge field.

        Returns:
            The text of the merge field.
        """
        GetDllLibDoc().MergeField_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_Text.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().MergeField_get_Text,self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        """
        Sets the text of the merge field.

        Args:
            value: The text to set.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().MergeField_set_Text.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().MergeField_set_Text,self.Ptr, valuePtr)

    @property

    def TextBefore(self)->str:
        """
        Returns or sets the text before the merge field.

        Returns:
            The text before the merge field.
        """
        GetDllLibDoc().MergeField_get_TextBefore.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_TextBefore.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().MergeField_get_TextBefore,self.Ptr))
        return ret


    @TextBefore.setter
    def TextBefore(self, value:str):
        """
        Sets the text before the merge field.

        Args:
            value: The text to set.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().MergeField_set_TextBefore.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().MergeField_set_TextBefore,self.Ptr, valuePtr)

    @property

    def TextAfter(self)->str:
        """
        Returns or sets the text after the merge field.

        Returns:
            The text after the merge field.
        """
        GetDllLibDoc().MergeField_get_TextAfter.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_TextAfter.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().MergeField_get_TextAfter,self.Ptr))
        return ret


    @TextAfter.setter
    def TextAfter(self, value:str):
        """
        Sets the text after the merge field.

        Args:
            value: The text to set.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().MergeField_set_TextAfter.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().MergeField_set_TextAfter,self.Ptr, valuePtr)

    @property

    def Prefix(self)->str:
        """
        Gets the prefix of the merge field.

        Returns:
            The prefix of the merge field.
        """
        GetDllLibDoc().MergeField_get_Prefix.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_Prefix.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().MergeField_get_Prefix,self.Ptr))
        return ret


    @property

    def NumberFormat(self)->str:
        """
        Gets the number format of the merge field.

        Returns:
            The number format of the merge field.
        """
        GetDllLibDoc().MergeField_get_NumberFormat.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_NumberFormat.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().MergeField_get_NumberFormat,self.Ptr))
        return ret


    @property

    def DateFormat(self)->str:
        """
        Gets the date format of the merge field.

        Returns:
            The date format of the merge field.
        """
        GetDllLibDoc().MergeField_get_DateFormat.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_DateFormat.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().MergeField_get_DateFormat,self.Ptr))
        return ret


    @property

    def TextItems(self)->'ParagraphItemCollection':
        """
        Gets the text items of the merge field.

        Returns:
            The text items of the merge field.
        """
        GetDllLibDoc().MergeField_get_TextItems.argtypes=[c_void_p]
        GetDllLibDoc().MergeField_get_TextItems.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().MergeField_get_TextItems,self.Ptr)
        ret = None if intPtr==None else ParagraphItemCollection(intPtr)
        return ret
