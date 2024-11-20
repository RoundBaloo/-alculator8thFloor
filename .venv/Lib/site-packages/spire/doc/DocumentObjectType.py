from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocumentObjectType(Enum):
    """
    Specifies the type of a Document object type.
    """
    Document = 0
    Section = 1
    Body = 2
    HeaderFooter = 3
    Paragraph = 4
    StructureDocumentTag = 5
    StructureDocumentTagInline = 6
    StructureDocumentTagRow = 7
    StructureDocumentTagCell = 8
    SDTBlockContent = 9
    SDTInlineContent = 10
    SDTRowContent = 11
    SDTCellContent = 12
    Table = 13
    TableRow = 14
    TableCell = 15
    TextRange = 16
    Picture = 17
    FieldStart = 18
    Field = 19
    FieldMark = 20
    FieldSeparator = 21
    FieldEnd = 22
    MergeField = 23
    SeqField = 24
    EmbededField = 25
    ControlField = 26
    TextFormField = 27
    DropDownFormField = 28
    CheckBox = 29
    BookmarkStart = 30
    BookmarkEnd = 31
    MoveFromRangeStart = 32
    MoveFromRangeEnd = 33
    MoveToRangeStart = 34
    MoveToRangeEnd = 35
    PermissionStart = 36
    PermissionEnd = 37
    Shape = 38
    ShapeGroup = 39
    ShapeLine = 40
    ShapePath = 41
    ShapeRect = 42
    Comment = 43
    Footnote = 44
    TextBox = 45
    Break = 46
    Symbol = 47
    TOC = 48
    XmlParaItem = 49
    Undefined = 50
    CommentMark = 51
    OleObject = 52
    CustomXml = 53
    SmartTag = 54
    OfficeMath = 55
    System = 56
    Ruby = 57
    Any = 58
    SubDocument = 59
    SpecialChar = 60
    GlossaryDocument = 61
    BuildingBlock = 62
    FormField = 63
