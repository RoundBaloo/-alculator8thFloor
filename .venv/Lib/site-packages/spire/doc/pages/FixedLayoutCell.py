from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc import *
from ctypes import *
import abc

class FixedLayoutCell (  BodyLayoutElement) :
    """
    <summary>
        Describes the cell within a table.
    </summary>
    """
    @property

    def Cell(self)->'TableCell':
        """
    <summary>
        Returns the cell that corresponds to the layout entity.  
    </summary>
        """
        GetDllLibDoc().FixedLayoutCell_get_Cell.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutCell_get_Cell.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutCell_get_Cell,self.Ptr)
        ret = None if intPtr==None else TableCell(intPtr)
        return ret


    @property

    def ParentNode(self)->'DocumentObject':
        """
    <summary>
        Provides the layout node that pertains to this particular entity.
    </summary>
        """
        GetDllLibDoc().FixedLayoutCell_get_ParentNode.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutCell_get_ParentNode.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutCell_get_ParentNode,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


