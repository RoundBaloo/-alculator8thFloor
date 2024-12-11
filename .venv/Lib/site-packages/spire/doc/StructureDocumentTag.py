from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class StructureDocumentTag (  BodyRegion, IBodyRegion, IStructureDocument, ICompositeObject) :
    """
    Represents a structured document tag.
    """
    @dispatch
    def __init__(self, doc:Document):
        """
        Initializes a new instance of the StructureDocumentTag class.
        :param doc: The document containing the structured document tag.
        """
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().StructureDocumentTag_CreateStructureDocumentTagD.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTag_CreateStructureDocumentTagD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTag_CreateStructureDocumentTagD,intPdoc)
        super(StructureDocumentTag, self).__init__(intPtr)

    @property

    def SDTContent(self)->'SDTContent':
        """
        Gets the last known contents of the structured document tag.
        :return: The last known contents of the structured document tag.
        """
        GetDllLibDoc().StructureDocumentTag_get_SDTContent.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTag_get_SDTContent.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTag_get_SDTContent,self.Ptr)
        ret = None if intPtr==None else SDTContent(intPtr)
        return ret


    @property

    def SDTProperties(self)->'SDTProperties':
        """
        Gets the properties of the structured document tag.
        :return: The properties of the structured document tag.
        """
        GetDllLibDoc().StructureDocumentTag_get_SDTProperties.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTag_get_SDTProperties.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTag_get_SDTProperties,self.Ptr)
        ret = None if intPtr==None else SDTProperties(intPtr)
        return ret


    @property

    def BreakCharacterFormat(self)->'CharacterFormat':
        """
        Gets the character format for the break symbol.
        :return: The character format for the break symbol.
        """
        GetDllLibDoc().StructureDocumentTag_get_BreakCharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTag_get_BreakCharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTag_get_BreakCharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the entity.
        :return: The type of the entity.
        """
        GetDllLibDoc().StructureDocumentTag_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTag_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().StructureDocumentTag_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the child entities.
        :return: The child entities.
        """
        GetDllLibDoc().StructureDocumentTag_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTag_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTag_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret



    def GetIndex(self ,entity:'IDocumentObject')->int:
        """
        Gets the index of the specified entity.
        :param entity: The entity to get the index of.
        :return: The index of the specified entity.
        """
        intPtrentity:c_void_p = entity.Ptr

        GetDllLibDoc().StructureDocumentTag_GetIndex.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().StructureDocumentTag_GetIndex.restype=c_int
        ret = CallCFunction(GetDllLibDoc().StructureDocumentTag_GetIndex,self.Ptr, intPtrentity)
        return ret

    def UpdateDataBinding(self):
        """
        Updates the data binding of the structured document tag.
        """
        GetDllLibDoc().StructureDocumentTag_UpdateDataBinding.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().StructureDocumentTag_UpdateDataBinding,self.Ptr)

#    @dispatch
#
#    def Replace(self ,pattern:'Regex',replace:str)->int:
#        """
#
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().StructureDocumentTag_Replace.argtypes=[c_void_p ,c_void_p,c_wchar_p]
#        GetDllLibDoc().StructureDocumentTag_Replace.restype=c_int
#        ret = GetDllLibDoc().StructureDocumentTag_Replace(self.Ptr, intPtrpattern,replace)
#        return ret


    @dispatch

    def Replace(self ,given:str,replace:str,caseSensitive:bool,wholeWord:bool)->int:
        """
        Replaces the specified text in the structured document tag.
        :param given: The text to replace.
        :param replace: The replacement text.
        :param caseSensitive: A flag indicating whether the replacement should be case-sensitive.
        :param wholeWord: A flag indicating whether the replacement should be done for whole words only.
        :return: The number of replacements made.
        """
        givenPtr = StrToPtr(given)
        replacePtr = StrToPtr(replace)
        GetDllLibDoc().StructureDocumentTag_ReplaceGRCW.argtypes=[c_void_p ,c_char_p,c_char_p,c_bool,c_bool]
        GetDllLibDoc().StructureDocumentTag_ReplaceGRCW.restype=c_int
        ret = CallCFunction(GetDllLibDoc().StructureDocumentTag_ReplaceGRCW,self.Ptr, givenPtr,replacePtr,caseSensitive,wholeWord)
        return ret

#    @dispatch
#
#    def Replace(self ,pattern:'Regex',textSelection:TextSelection)->int:
#        """
#
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#        intPtrtextSelection:c_void_p = textSelection.Ptr
#
#        GetDllLibDoc().StructureDocumentTag_ReplacePT.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().StructureDocumentTag_ReplacePT.restype=c_int
#        ret = GetDllLibDoc().StructureDocumentTag_ReplacePT(self.Ptr, intPtrpattern,intPtrtextSelection)
#        return ret


#    @dispatch
#
#    def Replace(self ,pattern:'Regex',textSelection:TextSelection,saveFormatting:bool)->int:
#        """
#
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#        intPtrtextSelection:c_void_p = textSelection.Ptr
#
#        GetDllLibDoc().StructureDocumentTag_ReplacePTS.argtypes=[c_void_p ,c_void_p,c_void_p,c_bool]
#        GetDllLibDoc().StructureDocumentTag_ReplacePTS.restype=c_int
#        ret = GetDllLibDoc().StructureDocumentTag_ReplacePTS(self.Ptr, intPtrpattern,intPtrtextSelection,saveFormatting)
#        return ret


    @dispatch

    def Replace(self ,given:str,textSelection:TextSelection,caseSensitive:bool,wholeWord:bool)->int:
        """
        Replaces the specified text in the structured document tag within the specified text selection.
        :param given: The text to replace.
        :param textSelection: The text selection within the structured document tag.
        :param caseSensitive: A flag indicating whether the replacement should be case-sensitive.
        :param wholeWord: A flag indicating whether the replacement should be done for whole words only.
        :return: The number of replacements made.
        """
        givenPtr = StrToPtr(given)
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().StructureDocumentTag_ReplaceGTCW.argtypes=[c_void_p ,c_char_p,c_void_p,c_bool,c_bool]
        GetDllLibDoc().StructureDocumentTag_ReplaceGTCW.restype=c_int
        ret = CallCFunction(GetDllLibDoc().StructureDocumentTag_ReplaceGTCW,self.Ptr, givenPtr,intPtrtextSelection,caseSensitive,wholeWord)
        return ret

    @dispatch

    def Replace(self ,given:str,textSelection:TextSelection,caseSensitive:bool,wholeWord:bool,saveFormatting:bool)->int:
        """
        Replaces the specified text in the structured document tag within the specified text selection and saves the formatting.
        :param given: The text to replace.
        :param textSelection: The text selection within the structured document tag.
        :param caseSensitive: A flag indicating whether the replacement should be case-sensitive.
        :param wholeWord: A flag indicating whether the replacement should be done for whole words only.
        :param saveFormatting: A flag indicating whether to save the formatting of the replaced text.
        :return: The number of replacements made.
        """
        givenPtr = StrToPtr(given)
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().StructureDocumentTag_ReplaceGTCWS.argtypes=[c_void_p ,c_char_p,c_void_p,c_bool,c_bool,c_bool]
        GetDllLibDoc().StructureDocumentTag_ReplaceGTCWS.restype=c_int
        ret = CallCFunction(GetDllLibDoc().StructureDocumentTag_ReplaceGTCWS,self.Ptr, givenPtr,intPtrtextSelection,caseSensitive,wholeWord,saveFormatting)
        return ret

#
#    def Find(self ,pattern:'Regex')->'TextSelection':
#        """
#
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().StructureDocumentTag_Find.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().StructureDocumentTag_Find.restype=c_void_p
#        intPtr = GetDllLibDoc().StructureDocumentTag_Find(self.Ptr, intPtrpattern)
#        ret = None if intPtr==None else TextSelection(intPtr)
#        return ret
#


