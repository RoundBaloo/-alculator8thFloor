from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Tab (  DocumentSerializable) :
    """
    Represents a tab in a document.
    """
    @property

    def Justification(self)->'TabJustification':
        """
        Gets or sets the justification of the tab.

        Returns:
            TabJustification: The justification of the tab.
        """
        GetDllLibDoc().Tab_get_Justification.argtypes=[c_void_p]
        GetDllLibDoc().Tab_get_Justification.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Tab_get_Justification,self.Ptr)
        objwraped = TabJustification(ret)
        return objwraped

    @Justification.setter
    def Justification(self, value:'TabJustification'):
        """
        Sets the justification of the tab.

        Args:
            value (TabJustification): The justification to set.
        """
        GetDllLibDoc().Tab_set_Justification.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Tab_set_Justification,self.Ptr, value.value)

    @property

    def TabLeader(self)->'TabLeader':
        """
        Gets or sets the tab leader.

        Returns:
            TabLeader: The tab leader.
        """
        GetDllLibDoc().Tab_get_TabLeader.argtypes=[c_void_p]
        GetDllLibDoc().Tab_get_TabLeader.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Tab_get_TabLeader,self.Ptr)
        objwraped = TabLeader(ret)
        return objwraped

    @TabLeader.setter
    def TabLeader(self, value:'TabLeader'):
        """
        Sets the tab leader.

        Args:
            value (TabLeader): The tab leader to set.
        """
        GetDllLibDoc().Tab_set_TabLeader.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Tab_set_TabLeader,self.Ptr, value.value)

    @property
    def Position(self)->float:
        """
        Gets or sets the position of the tab.

        Returns:
            float: The position of the tab.
        """
        GetDllLibDoc().Tab_get_Position.argtypes=[c_void_p]
        GetDllLibDoc().Tab_get_Position.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Tab_get_Position,self.Ptr)
        return ret

    @Position.setter
    def Position(self, value:float):
        """
        Sets the position of the tab.

        Args:
            value (float): The position to set.
        """
        GetDllLibDoc().Tab_set_Position.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Tab_set_Position,self.Ptr, value)


    def Equals(self ,tab:'Tab')->bool:
        """
        Determines whether the current tab is equal to the specified tab.

        Args:
            tab (Tab): The tab to compare.

        Returns:
            bool: True if the tabs are equal, False otherwise.
        """
        intPtrtab:c_void_p = tab.Ptr

        GetDllLibDoc().Tab_Equals.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Tab_Equals.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Tab_Equals,self.Ptr, intPtrtab)
        return ret

