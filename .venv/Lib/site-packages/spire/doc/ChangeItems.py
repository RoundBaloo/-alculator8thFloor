from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ChangeItems(SpireObject):
    """
    Eventhandler for DocumentObjectCollection class.

    Args:
        type (ChangeItemsType): DocumentObject type.
        entity (DocumentObject): The DocumentObject.
    """

    def Invoke(self ,type:'ChangeItemsType',entity:'DocumentObject'):
        """
        Invokes the event handler.

        Args:
            type (ChangeItemsType): DocumentObject type.
            entity (DocumentObject): The DocumentObject.
        """
        enumtype:c_int = type.value
        intPtrentity:c_void_p = entity.Ptr

        GetDllLibDoc().ChangeItems_Invoke.argtypes=[c_void_p ,c_int,c_void_p]
        CallCFunction(GetDllLibDoc().ChangeItems_Invoke,self.Ptr, enumtype,intPtrentity)

#
#    def BeginInvoke(self ,type:'ChangeItemsType',entity:'DocumentObject',callback:'AsyncCallback',object:'SpireObject')->'IAsyncResult':
#        """
#
#        """
#        enumtype:c_int = type.value
#        intPtrentity:c_void_p = entity.Ptr
#        intPtrcallback:c_void_p = callback.Ptr
#        intPtrobject:c_void_p = object.Ptr
#
#        GetDllLibDoc().ChangeItems_BeginInvoke.argtypes=[c_void_p ,c_int,c_void_p,c_void_p,c_void_p]
#        GetDllLibDoc().ChangeItems_BeginInvoke.restype=c_void_p
#        intPtr = GetDllLibDoc().ChangeItems_BeginInvoke(self.Ptr, enumtype,intPtrentity,intPtrcallback,intPtrobject)
#        ret = None if intPtr==None else IAsyncResult(intPtr)
#        return ret
#


#
#    def EndInvoke(self ,result:'IAsyncResult'):
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        GetDllLibDoc().ChangeItems_EndInvoke.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().ChangeItems_EndInvoke(self.Ptr, intPtrresult)


