from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class StructureDocumentTagCell (  TableCell, IStructureDocument) :
    """
    Represents a cell in a structured document tag.
    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the entity.
        """
        GetDllLibDoc().StructureDocumentTagCell_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagCell_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().StructureDocumentTagCell_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def SDTProperties(self)->'SDTProperties':
        """
        Gets the structured document tag properties.
        """
        GetDllLibDoc().StructureDocumentTagCell_get_SDTProperties.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagCell_get_SDTProperties.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTagCell_get_SDTProperties,self.Ptr)
        ret = None if intPtr==None else SDTProperties(intPtr)
        return ret


    @property

    def BreakCharacterFormat(self)->'CharacterFormat':
        """
        Gets character format for the break symbol.
        """
        GetDllLibDoc().StructureDocumentTagCell_get_BreakCharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagCell_get_BreakCharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTagCell_get_BreakCharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    def UpdateDataBinding(self):
        """
        Updates the data binding of the cell.
        """
        GetDllLibDoc().StructureDocumentTagCell_UpdateDataBinding.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().StructureDocumentTagCell_UpdateDataBinding,self.Ptr)

