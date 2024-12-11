from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CheckBoxFormField(FormField, IDocumentObject):
    """
    Represents a checkbox form field in a document.
    """
    @dispatch
    def __init__(self, doc:'IDocument'):
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().CheckBoxFormField_CreateCheckBoxFormFieldD.argtypes=[c_void_p]
        GetDllLibDoc().CheckBoxFormField_CreateCheckBoxFormFieldD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CheckBoxFormField_CreateCheckBoxFormFieldD,intPdoc)
        super(CheckBoxFormField, self).__init__(intPtr)
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.
        :return: The type of the document object.
        :rtype: DocumentObjectType
        """
        GetDllLibDoc().CheckBoxFormField_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().CheckBoxFormField_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CheckBoxFormField_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def CheckBoxSize(self)->int:
        """
        Gets or sets the size of the checkbox.
        :return: The size of the checkbox.
        :rtype: int
        """
        GetDllLibDoc().CheckBoxFormField_get_CheckBoxSize.argtypes=[c_void_p]
        GetDllLibDoc().CheckBoxFormField_get_CheckBoxSize.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CheckBoxFormField_get_CheckBoxSize,self.Ptr)
        return ret

    @CheckBoxSize.setter
    def CheckBoxSize(self, value:int):
        """
        Sets the size of the checkbox.
        :param value: The size of the checkbox.
        :type value: int
        """
        GetDllLibDoc().CheckBoxFormField_set_CheckBoxSize.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().CheckBoxFormField_set_CheckBoxSize,self.Ptr, value)

    @property
    def DefaultCheckBoxValue(self)->bool:
        """
        Gets or sets the default checkbox value.
        :return: The default checkbox value.
        :rtype: bool
        """
        GetDllLibDoc().CheckBoxFormField_get_DefaultCheckBoxValue.argtypes=[c_void_p]
        GetDllLibDoc().CheckBoxFormField_get_DefaultCheckBoxValue.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().CheckBoxFormField_get_DefaultCheckBoxValue,self.Ptr)
        return ret

    @DefaultCheckBoxValue.setter
    def DefaultCheckBoxValue(self, value:bool):
        """
        Sets the default checkbox value.
        :param value: The default checkbox value.
        :type value: bool
        """
        GetDllLibDoc().CheckBoxFormField_set_DefaultCheckBoxValue.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().CheckBoxFormField_set_DefaultCheckBoxValue,self.Ptr, value)

    @property
    def Checked(self)->bool:
        """
        Gets or sets the Checked property.
        :return: The Checked property.
        :rtype: bool
        """
        GetDllLibDoc().CheckBoxFormField_get_Checked.argtypes=[c_void_p]
        GetDllLibDoc().CheckBoxFormField_get_Checked.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().CheckBoxFormField_get_Checked,self.Ptr)
        return ret

    @Checked.setter
    def Checked(self, value:bool):
        """
        Sets the Checked property.
        :param value: The Checked property.
        :type value: bool
        """
        GetDllLibDoc().CheckBoxFormField_set_Checked.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().CheckBoxFormField_set_Checked,self.Ptr, value)

    @property

    def SizeType(self)->'CheckBoxSizeType':
        """
        Gets or sets the check box size type.
        :return: The check box size type.
        :rtype: CheckBoxSizeType
        """
        GetDllLibDoc().CheckBoxFormField_get_SizeType.argtypes=[c_void_p]
        GetDllLibDoc().CheckBoxFormField_get_SizeType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CheckBoxFormField_get_SizeType,self.Ptr)
        objwraped = CheckBoxSizeType(ret)
        return objwraped

    @SizeType.setter
    def SizeType(self, value:'CheckBoxSizeType'):
        """
        Sets the check box size type.
        :param value: The check box size type.
        :type value: CheckBoxSizeType
        """
        GetDllLibDoc().CheckBoxFormField_set_SizeType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().CheckBoxFormField_set_SizeType,self.Ptr, value.value)

