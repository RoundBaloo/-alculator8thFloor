from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TabCollection (  DocumentSerializableCollection) :
    """
    Represents a collection of Tab objects for paragraph or paragraph format.
    """

    def get_Item(self ,index:int)->'Tab':
        """
        Gets the Tab at the specified index.

        Args:
            index: The index of the Tab.

        Returns:
            The Tab at the specified index.
        """
        
        GetDllLibDoc().TabCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TabCollection_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TabCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else Tab(intPtr)
        return ret


    @dispatch

    def AddTab(self)->Tab:
        """
        Adds a Tab.

        Returns:
            The added Tab.
        """
        GetDllLibDoc().TabCollection_AddTab.argtypes=[c_void_p]
        GetDllLibDoc().TabCollection_AddTab.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TabCollection_AddTab,self.Ptr)
        ret = None if intPtr==None else Tab(intPtr)
        return ret


    @dispatch

    def AddTab(self ,position:float,justification:TabJustification,leader:TabLeader)->Tab:
        """
        Adds a Tab with specified position, justification, and leader.

        Args:
            position: The position of the Tab.
            justification: The justification of the Tab.
            leader: The leader of the Tab.

        Returns:
            The added Tab.
        """
        enumjustification:c_int = justification.value
        enumleader:c_int = leader.value

        GetDllLibDoc().TabCollection_AddTabPJL.argtypes=[c_void_p ,c_float,c_int,c_int]
        GetDllLibDoc().TabCollection_AddTabPJL.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TabCollection_AddTabPJL,self.Ptr, position,enumjustification,enumleader)
        ret = None if intPtr==None else Tab(intPtr)
        return ret


    @dispatch

    def AddTab(self ,position:float)->Tab:
        """
        Adds a Tab with specified position.

        Args:
            position: The position of the Tab.

        Returns:
            The added Tab.
        """
        
        GetDllLibDoc().TabCollection_AddTabP.argtypes=[c_void_p ,c_float]
        GetDllLibDoc().TabCollection_AddTabP.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TabCollection_AddTabP,self.Ptr, position)
        ret = None if intPtr==None else Tab(intPtr)
        return ret


    def Clear(self):
        """
        Removes all the tabs from the tab collection.
        """
        GetDllLibDoc().TabCollection_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().TabCollection_Clear,self.Ptr)


    def RemoveAt(self ,index:int):
        """
        Removes the tab at the specified index from the tab collection.

        Args:
            index: The index of the tab to remove.
        """
        
        GetDllLibDoc().TabCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().TabCollection_RemoveAt,self.Ptr, index)

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """
        Determines whether the current TabCollection is equal to the specified object.

        Args:
            obj: The object to compare with the current TabCollection.

        Returns:
            True if the current TabCollection is equal to the specified object, False otherwise.
        """
        intPtrobj:c_void_p = obj.Ptr

        GetDllLibDoc().TabCollection_Equals.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TabCollection_Equals.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TabCollection_Equals,self.Ptr, intPtrobj)
        return ret

    @dispatch

    def Equals(self ,other:'TabCollection')->bool:
        """
        Determines whether the current TabCollection is equal to the specified TabCollection.

        Args:
            other: The TabCollection to compare with the current TabCollection.

        Returns:
            True if the current TabCollection is equal to the specified TabCollection, False otherwise.
        """
        intPtrother:c_void_p = other.Ptr

        GetDllLibDoc().TabCollection_EqualsO.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().TabCollection_EqualsO.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TabCollection_EqualsO,self.Ptr, intPtrother)
        return ret

