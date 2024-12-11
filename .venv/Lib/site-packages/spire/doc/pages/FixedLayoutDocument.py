from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc import *
from spire.doc.pages import *
from ctypes import *
import abc

class FixedLayoutDocument (  LayoutElement) :
    """

    """
    def __init__(self, doc:'Document'):
        """
        """
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().FixedLayoutDocument_CreateFixedLayoutDocumentD.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutDocument_CreateFixedLayoutDocumentD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutDocument_CreateFixedLayoutDocumentD,intPdoc)
        super(FixedLayoutDocument, self).__init__(intPtr)
    @property

    def Pages(self)->'LayoutFixedLPagesCollection':
        """
    <summary>
        Provides access to the pages of a document.
    </summary>
        """
        GetDllLibDoc().FixedLayoutDocument_get_Pages.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutDocument_get_Pages.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutDocument_get_Pages,self.Ptr)
        from spire.doc.pages.LayoutFixedLPagesCollection import LayoutFixedLPagesCollection
        ret = None if intPtr==None else LayoutFixedLPagesCollection(intPtr)
        return ret



    @property

    def ParentNode(self)->'DocumentObject':
        """
    <summary>
        Provides the layout node that pertains to this particular entity.
    </summary>
        """
        GetDllLibDoc().FixedLayoutDocument_get_ParentNode.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutDocument_get_ParentNode.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutDocument_get_ParentNode,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret



    def GetLayoutEntitiesOfNode(self ,node:'DocumentObject')->'LayoutCollection':
        """
    <summary>
        Returns all the layout entities of the specified node.
    </summary>
        """
        intPtrnode:c_void_p = node.Ptr

        GetDllLibDoc().FixedLayoutDocument_GetLayoutEntitiesOfNode.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().FixedLayoutDocument_GetLayoutEntitiesOfNode.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutDocument_GetLayoutEntitiesOfNode,self.Ptr, intPtrnode)
        from spire.doc.pages.LayoutCollection import LayoutCollection
        ret = None if intPtr==None else LayoutCollection(intPtr)
        return ret



