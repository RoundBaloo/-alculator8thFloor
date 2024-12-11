from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc import *
from ctypes import *
import abc

class FixedLayoutEndnote (  BodyLayoutElement) :
    """
    <summary>
        Represents placeholder for endnote content.
    </summary>
    """
    @property

    def Endnote(self)->'Footnote':
        """
    <summary>
        Returns the endnote that corresponds to the layout entity.  
    </summary>
        """
        GetDllLibDoc().FixedLayoutEndnote_get_Endnote.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutEndnote_get_Endnote.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutEndnote_get_Endnote,self.Ptr)
        ret = None if intPtr==None else Footnote(intPtr)
        return ret


    @property

    def ParentNode(self)->'DocumentObject':
        """
    <summary>
        Provides the layout node that pertains to this particular entity.
    </summary>
        """
        GetDllLibDoc().FixedLayoutEndnote_get_ParentNode.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutEndnote_get_ParentNode.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutEndnote_get_ParentNode,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


