from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextFormField (  FormField, ITextRange) :
    """
    Represents a text form field in a document.
    """
    @dispatch
    def __init__(self, doc:IDocument):
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().TextFormField_CreateTextFormFieldD.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_CreateTextFormFieldD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextFormField_CreateTextFormFieldD,intPdoc)
        super(TextFormField, self).__init__(intPtr)
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.

        Returns:
            DocumentObjectType: The type of the document object.
        """
        GetDllLibDoc().TextFormField_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextFormField_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def TextFieldType(self)->'TextFormFieldType':
        """
        Gets or sets the text form field type.

        Returns:
            TextFormFieldType: The text form field type.
        """
        GetDllLibDoc().TextFormField_get_TextFieldType.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_TextFieldType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextFormField_get_TextFieldType,self.Ptr)
        objwraped = TextFormFieldType(ret)
        return objwraped

    @TextFieldType.setter
    def TextFieldType(self, value:'TextFormFieldType'):
        """
        Sets the text form field type.

        Args:
            value (TextFormFieldType): The text form field type.
        """
        GetDllLibDoc().TextFormField_set_TextFieldType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextFormField_set_TextFieldType,self.Ptr, value.value)

    @property

    def StringFormat(self)->str:
        """
        Gets or sets the string text format (text, date/time, number) directly.

        Returns:
            str: The string text format.
        """
        GetDllLibDoc().TextFormField_get_StringFormat.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_StringFormat.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().TextFormField_get_StringFormat,self.Ptr))
        return ret


    @StringFormat.setter
    def StringFormat(self, value:str):
        """
        Sets the string text format (text, date/time, number) directly.

        Args:
            value (str): The string text format.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TextFormField_set_StringFormat.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().TextFormField_set_StringFormat,self.Ptr, valuePtr)

    @property

    def DefaultText(self)->str:
        """
        Gets or sets the default text for the text form field.

        Returns:
            str: The default text.
        """
        GetDllLibDoc().TextFormField_get_DefaultText.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_DefaultText.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().TextFormField_get_DefaultText,self.Ptr))
        return ret


    @DefaultText.setter
    def DefaultText(self, value:str):
        """
        Sets the default text for the text form field.

        Args:
            value (str): The default text.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TextFormField_set_DefaultText.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().TextFormField_set_DefaultText,self.Ptr, valuePtr)

    @property
    def MaximumLength(self)->int:
        """
        Gets or sets the maximum text length.

        Returns:
            int: The maximum text length.
        """
        GetDllLibDoc().TextFormField_get_MaximumLength.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_MaximumLength.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextFormField_get_MaximumLength,self.Ptr)
        return ret

    @MaximumLength.setter
    def MaximumLength(self, value:int):
        """
        Sets the maximum text length.

        Args:
            value (int): The maximum text length.
        """
        GetDllLibDoc().TextFormField_set_MaximumLength.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextFormField_set_MaximumLength,self.Ptr, value)

    @property

    def TextRange(self)->'TextRange':
        """
        Gets or sets the form field text range.

        Returns:
            TextRange: The form field text range.
        """
        GetDllLibDoc().TextFormField_get_TextRange.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_TextRange.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextFormField_get_TextRange,self.Ptr)
        ret = None if intPtr==None else TextRange(intPtr)
        return ret


    @TextRange.setter
    def TextRange(self, value:'TextRange'):
        """
        Sets the form field text range.

        Args:
            value (TextRange): The form field text range.
        """
        GetDllLibDoc().TextFormField_set_TextRange.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().TextFormField_set_TextRange,self.Ptr, value.Ptr)

    @property

    def Text(self)->str:
        """
        Gets or sets the text of the text form field.

        Returns:
            str: The text of the text form field.
        """
        GetDllLibDoc().TextFormField_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().TextFormField_get_Text.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().TextFormField_get_Text,self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        """
        Sets the text of the text form field.

        Args:
            value (str): The text of the text form field.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TextFormField_set_Text.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().TextFormField_set_Text,self.Ptr, valuePtr)

