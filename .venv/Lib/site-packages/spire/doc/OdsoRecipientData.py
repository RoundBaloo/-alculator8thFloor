from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class OdsoRecipientData (SpireObject) :
    """
    Represents recipient data for an ODSO (Office Data Source Object) document.
    """

    def Clone(self)->'OdsoRecipientData':
        """
        Creates a copy of the OdsoRecipientData object.

        Returns:
            OdsoRecipientData: The cloned OdsoRecipientData object.
        """
        GetDllLibDoc().OdsoRecipientData_Clone.argtypes=[c_void_p]
        GetDllLibDoc().OdsoRecipientData_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().OdsoRecipientData_Clone,self.Ptr)
        ret = None if intPtr==None else OdsoRecipientData(intPtr)
        return ret


    @property
    def Active(self)->bool:
        """
        Gets or sets a value indicating whether the recipient is active.

        Returns:
            bool: True if the recipient is active, False otherwise.
        """
        GetDllLibDoc().OdsoRecipientData_get_Active.argtypes=[c_void_p]
        GetDllLibDoc().OdsoRecipientData_get_Active.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().OdsoRecipientData_get_Active,self.Ptr)
        return ret

    @Active.setter
    def Active(self, value:bool):
        """
        Sets a value indicating whether the recipient is active.

        Args:
            value (bool): True if the recipient is active, False otherwise.
        """
        GetDllLibDoc().OdsoRecipientData_set_Active.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().OdsoRecipientData_set_Active,self.Ptr, value)

    @property
    def Column(self)->int:
        """
        Gets or sets the column index of the recipient.

        Returns:
            int: The column index of the recipient.
        """
        GetDllLibDoc().OdsoRecipientData_get_Column.argtypes=[c_void_p]
        GetDllLibDoc().OdsoRecipientData_get_Column.restype=c_int
        ret = CallCFunction(GetDllLibDoc().OdsoRecipientData_get_Column,self.Ptr)
        return ret

    @Column.setter
    def Column(self, value:int):
        """
        Sets the column index of the recipient.

        Args:
            value (int): The column index of the recipient.
        """
        GetDllLibDoc().OdsoRecipientData_set_Column.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().OdsoRecipientData_set_Column,self.Ptr, value)

#    @property
#
#    def UniqueTag(self)->List['Byte']:
#        """
#
#        """
#        GetDllLibDoc().OdsoRecipientData_get_UniqueTag.argtypes=[c_void_p]
#        GetDllLibDoc().OdsoRecipientData_get_UniqueTag.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().OdsoRecipientData_get_UniqueTag(self.Ptr)
#        ret = GetVectorFromArray(intPtrArray, Byte)
#        return ret


#    @UniqueTag.setter
#    def UniqueTag(self, value:List['Byte']):
#        vCount = len(value)
#        ArrayType = c_void_p * vCount
#        vArray = ArrayType()
#        for i in range(0, vCount):
#            vArray[i] = value[i].Ptr
#        GetDllLibDoc().OdsoRecipientData_set_UniqueTag.argtypes=[c_void_p, ArrayType, c_int]
#        GetDllLibDoc().OdsoRecipientData_set_UniqueTag(self.Ptr, vArray, vCount)


    @property
    def Hash(self)->int:
        """
        Gets or sets the hash value of the recipient.

        Returns:
            int: The hash value of the recipient.
        """
        GetDllLibDoc().OdsoRecipientData_get_Hash.argtypes=[c_void_p]
        GetDllLibDoc().OdsoRecipientData_get_Hash.restype=c_int
        ret = CallCFunction(GetDllLibDoc().OdsoRecipientData_get_Hash,self.Ptr)
        return ret

    @Hash.setter
    def Hash(self, value:int):
        """
        Sets the hash value of the recipient.

        Args:
            value (int): The hash value of the recipient.
        """
        GetDllLibDoc().OdsoRecipientData_set_Hash.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().OdsoRecipientData_set_Hash,self.Ptr, value)

