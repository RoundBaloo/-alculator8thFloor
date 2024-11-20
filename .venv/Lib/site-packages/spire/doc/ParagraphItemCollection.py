from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ParagraphItemCollection (  DocumentObjectCollection) :
    """
    Represents a collection for Paragraph child items.
    """

    def get_Item(self ,index:int)->'ParagraphBase':
        """
        Get the item at the specified index.

        Args:
            index: The index of the item.

        Returns:
            The item at the specified index.
        """
        
        GetDllLibDoc().ParagraphItemCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ParagraphItemCollection_get_Item.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().ParagraphItemCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else self._create(intPtr)
        return ret


    def _create(self, intPtrWithTypeName:IntPtrWithTypeName)->'ParagraphBase':
		
        ret= None
        if intPtrWithTypeName == None :
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
		
        if (strName == "Spire.Doc.PictureWatermark"):
            from spire.doc import PictureWatermark
            ret = PictureWatermark(intPtr)
        elif (strName == "Spire.Doc.TextWatermark"):
            from spire.doc import TextWatermark
            ret = TextWatermark(intPtr)
        elif (strName == "Spire.Doc.WatermarkBase"):
            from spire.doc import WatermarkBase
            ret = WatermarkBase(intPtr)
        elif (strName == "Spire.Doc.Fields.OMath.OfficeMath"):
            from spire.doc import OfficeMath
            ret = OfficeMath(intPtr)
        elif (strName == "Spire.Doc.BookmarkEnd"):
            from spire.doc import BookmarkEnd
            ret = BookmarkEnd(intPtr)
        elif (strName == "Spire.Doc.BookmarkStart"):
            from spire.doc import BookmarkStart
            ret = BookmarkStart(intPtr)
        elif (strName == "Spire.Doc.Break"):
            from spire.doc import Break
            ret = Break(intPtr)
        elif (strName == "Spire.Doc.Fields.ShapeGroup"):
            from spire.doc import ShapeGroup
            ret = ShapeGroup(intPtr)
        elif (strName == "Spire.Doc.Fields.DocOleObject"):
            from spire.doc import DocOleObject
            ret = DocOleObject(intPtr)
        elif (strName == "Spire.Doc.PermissionEnd"):
            from spire.doc import PermissionEnd
            ret = PermissionEnd(intPtr)
        elif (strName == "Spire.Doc.PermissionStart"):
            from spire.doc import PermissionStart
            ret = PermissionStart(intPtr)
        elif (strName == "Spire.Doc.Fields.Shape.ShapeBase"):
            from spire.doc import ShapeBase
            ret = ShapeBase(intPtr)
        elif (strName == "Spire.Doc.Fields.ShapeObject"):
            from spire.doc import ShapeObject
            ret = ShapeObject(intPtr)
        elif (strName == "Spire.Doc.Fields.TableOfContent"):
            from spire.doc import TableOfContent
            ret = TableOfContent(intPtr)
        elif (strName == "Spire.Doc.Fields.CheckBoxFormField"):
            from spire.doc import CheckBoxFormField
            ret = CheckBoxFormField(intPtr)
        elif (strName == "Spire.Doc.Fields.Comment"):
            from spire.doc import Comment
            ret = Comment(intPtr)
        elif (strName == "Spire.Doc.Documents.CommentMark"):
            from spire.doc import CommentMark
            ret = CommentMark(intPtr)
        elif (strName == "Spire.Doc.Fields.DropDownFormField"):
            from spire.doc import DropDownFormField
            ret = DropDownFormField(intPtr)
        elif (strName == "Spire.Doc.Fields.ControlField"):
            from spire.doc import ControlField
            ret = ControlField(intPtr)
        elif (strName == "Spire.Doc.Fields.Field"):
            from spire.doc import Field
            ret = Field(intPtr)
        elif (strName == "Spire.Doc.Fields.FieldMark"):
            from spire.doc import FieldMark
            ret = FieldMark(intPtr)
        elif (strName == "Spire.Doc.Fields.Footnote"):
            from spire.doc import Footnote
            ret = Footnote(intPtr)
        elif (strName == "Spire.Doc.Fields.FormField"):
            from spire.doc import FormField
            ret = FormField(intPtr)
        elif (strName == "Spire.Doc.Fields.IfField"):
            from spire.doc import IfField
            ret = IfField(intPtr)
        elif (strName == "Spire.Doc.Fields.MergeField"):
            from spire.doc import MergeField
            ret = MergeField(intPtr)
        elif (strName == "Spire.Doc.Fields.DocPicture"):
            from spire.doc import DocPicture
            ret = DocPicture(intPtr)
        elif (strName == "Spire.Doc.Fields.SequenceField"):
            from spire.doc import SequenceField
            ret = SequenceField(intPtr)
        elif (strName == "Spire.Doc.Fields.Symbol"):
            from spire.doc import Symbol
            ret = Symbol(intPtr)
        elif (strName == "Spire.Doc.Fields.TextBox"):
            from spire.doc import TextBox
            ret = TextBox(intPtr)
        elif (strName == "Spire.Doc.Fields.TextFormField"):
            from spire.doc import TextFormField
            ret = TextFormField(intPtr)
        elif (strName == "Spire.Doc.Fields.TextRange"):
            from spire.doc import TextRange
            ret = TextRange(intPtr)
        elif (strName == "Spire.Doc.Documents.StructureDocumentTagInline"):
            from spire.doc import StructureDocumentTagInline
            ret = StructureDocumentTagInline(intPtr)
        else:
            ret = ParagraphBase(intPtr)
        return ret;
		
