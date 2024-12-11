from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc import *
from ctypes import *
import abc

class FixedLayoutComment (  BodyLayoutElement) :
    """
    <summary>
        Represents placeholder for comment content.
    </summary>
    """
    @property

    def Comment(self)->'Comment':
        """
    <summary>
        Returns the comment that corresponds to the layout entity.  
    </summary>
        """
        GetDllLibDoc().FixedLayoutComment_get_Comment.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutComment_get_Comment.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutComment_get_Comment,self.Ptr)
        ret = None if intPtr==None else Comment(intPtr)
        return ret


    @property

    def ParentNode(self)->'DocumentObject':
        """
    <summary>
        Provides the layout node that pertains to this particular entity. 
    </summary>
        """
        GetDllLibDoc().FixedLayoutComment_get_ParentNode.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutComment_get_ParentNode.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutComment_get_ParentNode,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


