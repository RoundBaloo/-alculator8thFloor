from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc import *
from ctypes import *
import abc

class FixedLayoutHeaderFooter (  BodyLayoutElement) :
    """
    <summary>
        Represents the header/footer content on a page.
    </summary>
    """
    @property

    def Kind(self)->str:
        """
    <summary>
        Returns the type of the header or footer.
    </summary>
        """
        GetDllLibDoc().FixedLayoutHeaderFooter_get_Kind.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutHeaderFooter_get_Kind.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().FixedLayoutHeaderFooter_get_Kind,self.Ptr))
        return ret


