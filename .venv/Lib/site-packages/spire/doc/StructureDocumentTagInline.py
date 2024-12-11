from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class StructureDocumentTagInline (  ParagraphBase, IStructureDocument, ICompositeObject) :
    """
    Represents a structured document tag around one or more inline-level structures.
    """
    @dispatch
    def __init__(self, doc:Document):
        """
        Initializes a new instance of the StructureDocumentTagInline class.

        Args:
            doc (Document): The document containing the structured document tag.
        """
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().StructureDocumentTagInline_CreateStructureDocumentTagInlineD.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_CreateStructureDocumentTagInlineD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTagInline_CreateStructureDocumentTagInlineD,intPdoc)
        super(StructureDocumentTagInline, self).__init__(intPtr)

    @property

    def SDTContent(self)->'SDTInlineContent':
        """
        Gets the last known contents of the structured document tag.

        Returns:
            SDTInlineContent: The last known contents of the structured document tag.
        """
        GetDllLibDoc().StructureDocumentTagInline_get_SDTContent.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_get_SDTContent.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTagInline_get_SDTContent,self.Ptr)
        ret = None if intPtr==None else SDTInlineContent(intPtr)
        return ret


    @property

    def SDTProperties(self)->'SDTProperties':
        """
        Gets the properties of the structured document tag.

        Returns:
            SDTProperties: The properties of the structured document tag.
        """
        GetDllLibDoc().StructureDocumentTagInline_get_SDTProperties.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_get_SDTProperties.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTagInline_get_SDTProperties,self.Ptr)
        ret = None if intPtr==None else SDTProperties(intPtr)
        return ret


    @property

    def BreakCharacterFormat(self)->'CharacterFormat':
        """
        Gets the character format for the break symbol.

        Returns:
            CharacterFormat: The character format for the break symbol.
        """
        GetDllLibDoc().StructureDocumentTagInline_get_BreakCharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_get_BreakCharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTagInline_get_BreakCharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the entity.

        Returns:
            DocumentObjectType: The type of the entity.
        """
        GetDllLibDoc().StructureDocumentTagInline_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().StructureDocumentTagInline_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the child entities.

        Returns:
            DocumentObjectCollection: The child entities.
        """
        GetDllLibDoc().StructureDocumentTagInline_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagInline_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTagInline_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    def BackupChildObjects(self):
        """
        Backs up the child entities.
        """
        GetDllLibDoc().StructureDocumentTagInline_BackupChildObjects.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().StructureDocumentTagInline_BackupChildObjects,self.Ptr)

    def RevertChildObjects(self):
        """
        Reverts the child entities.
        """
        GetDllLibDoc().StructureDocumentTagInline_RevertChildObjects.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().StructureDocumentTagInline_RevertChildObjects,self.Ptr)


    def MakeChanges(self ,acceptChanges:bool):
        """
        Makes changes to the structured document tag.

        Args:
            acceptChanges (bool): A value indicating whether to accept the changes.
        """
        
        GetDllLibDoc().StructureDocumentTagInline_MakeChanges.argtypes=[c_void_p ,c_bool]
        CallCFunction(GetDllLibDoc().StructureDocumentTagInline_MakeChanges,self.Ptr, acceptChanges)

    def UpdateDataBinding(self):
        """
        Updates the data binding of the structured document tag.
        """
        GetDllLibDoc().StructureDocumentTagInline_UpdateDataBinding.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().StructureDocumentTagInline_UpdateDataBinding,self.Ptr)

