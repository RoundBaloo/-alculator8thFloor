from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class VariableCollection (  IEnumerable) :
    """
    Represents a collection of variables.
    """

    def get_Item(self ,name:str)->str:
        """
        Gets the variable with the specified name.

        Args:
            name: The name of the variable.

        Returns:
            The value of the variable.
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().VariableCollection_get_Item.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().VariableCollection_get_Item.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().VariableCollection_get_Item,self.Ptr, namePtr))
        return ret



    def set_Item(self ,name:str,value:str):
        """
        Sets the value of the variable with the specified name.

        Args:
            name: The name of the variable.
            value: The value to set.
        """
        namePtr = StrToPtr(name)
        valuePtr = StrToPtr(value)
        GetDllLibDoc().VariableCollection_set_Item.argtypes=[c_void_p ,c_char_p,c_char_p]
        CallCFunction(GetDllLibDoc().VariableCollection_set_Item,self.Ptr, namePtr,valuePtr)

    @property
    def Count(self)->int:
        """
        Gets the count of variables.

        Returns:
            The count of variables.
        """
        GetDllLibDoc().VariableCollection_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().VariableCollection_get_Count.restype=c_int
        ret = CallCFunction(GetDllLibDoc().VariableCollection_get_Count,self.Ptr)
        return ret


    def Add(self ,name:str,value:str):
        """
        Adds a variable to the collection.

        Args:
            name: The name of the variable.
            value: The value of the variable.
        """
        namePtr = StrToPtr(name)
        valuePtr = StrToPtr(value)
        GetDllLibDoc().VariableCollection_Add.argtypes=[c_void_p ,c_char_p,c_char_p]
        CallCFunction(GetDllLibDoc().VariableCollection_Add,self.Ptr, namePtr,valuePtr)


    def GetNameByIndex(self ,index:int)->str:
        """
        Gets the name of the variable at the specified index.

        Args:
            index: The index of the variable.

        Returns:
            The name of the variable.
        """
        
        GetDllLibDoc().VariableCollection_GetNameByIndex.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().VariableCollection_GetNameByIndex.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().VariableCollection_GetNameByIndex,self.Ptr, index))
        return ret



    def GetValueByIndex(self ,index:int)->str:
        """
        Gets the value of the variable at the specified index.

        Args:
            index: The index of the variable.

        Returns:
            The value of the variable.
        """
        
        GetDllLibDoc().VariableCollection_GetValueByIndex.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().VariableCollection_GetValueByIndex.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().VariableCollection_GetValueByIndex,self.Ptr, index))
        return ret



    def Remove(self ,name:str):
        """
        Removes the variable with the specified name from the collection.

        Args:
            name: The name of the variable to remove.
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().VariableCollection_Remove.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().VariableCollection_Remove,self.Ptr, namePtr)


    def GetEnumerator(self)->'IEnumerator':
        """
        Gets an enumerator for the collection.

        Returns:
            An enumerator for the collection.
        """
        GetDllLibDoc().VariableCollection_GetEnumerator.argtypes=[c_void_p]
        GetDllLibDoc().VariableCollection_GetEnumerator.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().VariableCollection_GetEnumerator,self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret


