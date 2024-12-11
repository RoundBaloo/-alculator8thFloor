from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Break (  ParagraphBase, IDocumentObject) :
    """
    Represents a break in a document.
    """
    @dispatch
    def __init__(self, doc: 'IDocument'):
        """
        Initializes a new instance of the Break class with the specified document.
        
        Args:
            doc: The document to which the break belongs.
        """
        intPdoc: c_void_p = doc.Ptr

        GetDllLibDoc().Break_CreateBreakD.argtypes=[c_void_p]
        GetDllLibDoc().Break_CreateBreakD.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Break_CreateBreakD,intPdoc)
        super(Break, self).__init__(intPtr)

    @dispatch
    def __init__(self, doc: 'IDocument', breakType: BreakType):
        """
        Initializes a new instance of the Break class with the specified document and break type.
        
        Args:
            doc: The document to which the break belongs.
            breakType: The type of the break.
        """
        intPdoc: c_void_p = doc.Ptr
        iTypebreakType: c_int = breakType.value

        GetDllLibDoc().Break_CreateBreakDB.argtypes = [c_void_p,c_int]
        GetDllLibDoc().Break_CreateBreakDB.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Break_CreateBreakDB,intPdoc,iTypebreakType)
        super(Break, self).__init__(intPtr)

    @property
    def DocumentObjectType(self) -> DocumentObjectType:
        """
        Gets the type of the document object.
        
        Returns:
            The type of the document object.
        """
        GetDllLibDoc().Break_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Break_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Break_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def CharacterFormat(self) -> 'CharacterFormat':
        """
        Gets the character format.
        
        Returns:
            The character format.
        """
        GetDllLibDoc().Break_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().Break_get_CharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Break_get_CharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property
    def BreakType(self) -> BreakType:
        """
        Gets the type of the break.
        
        Returns:
            The type of the break.
        """
        GetDllLibDoc().Break_get_BreakType.argtypes=[c_void_p]
        GetDllLibDoc().Break_get_BreakType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Break_get_BreakType,self.Ptr)
        objwraped = BreakType(ret)
        return objwraped

