from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc import *
from ctypes import *
import abc

class FixedLayoutTextBox (  BodyLayoutElement) :
    """
    <summary>
        Represents text area inside of a shape.
    </summary>
    """
    @property

    def ParentNode(self)->'DocumentObject':
        """
    <summary>
        Provides the layout node that pertains to this particular entity.
    </summary>
        """
        GetDllLibDoc().FixedLayoutTextBox_get_ParentNode.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutTextBox_get_ParentNode.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutTextBox_get_ParentNode,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


