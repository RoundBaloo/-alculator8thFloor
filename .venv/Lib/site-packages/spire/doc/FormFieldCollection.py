from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FormFieldCollection (  CollectionEx) :
    """
    Represents a collection of form fields.
    """
    @dispatch

    def get_Item(self ,index:int)->FormField:
        """
        Gets the formField at the specified index.
        """
        
        GetDllLibDoc().FormFieldCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().FormFieldCollection_get_Item.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().FormFieldCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else self._createDocumentObject(intPtr)
        return ret

    def _createDocumentObject(self, intPtrWithTypeName:IntPtrWithTypeName)->FormField:
        ret= None
        if intPtrWithTypeName == None :
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName == "Spire.Doc.Fields.CheckBoxFormField"):
            from spire.doc import CheckBoxFormField
            ret = CheckBoxFormField(intPtr)
        elif(strName == "Spire.Doc.Fields.DropDownFormField"):
            from spire.doc import DropDownFormField
            ret = DropDownFormField(intPtr)
        elif(strName == "Spire.Doc.Fields.TextFormField"):
            from spire.doc import TextFormField
            ret = TextFormField(intPtr)
        else:
            ret = FormField(intPtr)

        return ret

    @dispatch

    def get_Item(self ,formFieldName:str)->FormField:
        """
        Gets the formField by specified form field name.
        """
        formFieldNamePtr = StrToPtr(formFieldName)
        GetDllLibDoc().FormFieldCollection_get_ItemF.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().FormFieldCollection_get_ItemF.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FormFieldCollection_get_ItemF,self.Ptr, formFieldNamePtr)
        ret = None if intPtr==None else FormField(intPtr)
        return ret



    def ContainsName(self ,itemName:str)->bool:
        """
        Determines whether the specified collection contains item with specified name.
        """
        itemNamePtr = StrToPtr(itemName)
        GetDllLibDoc().FormFieldCollection_ContainsName.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().FormFieldCollection_ContainsName.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().FormFieldCollection_ContainsName,self.Ptr, itemNamePtr)
        return ret

