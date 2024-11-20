from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ParagraphItemType(Enum):
    """
    Specifies the type of the ParagraphBase.
    """
    TextRange = 0
    Picture = 1
    Field = 2
    FieldMark = 3
    MergeField = 4
    FormField = 5
    CheckBox = 6
    TextFormField = 7
    DropDownFormField = 8
    SeqField = 9
    EmbedField = 10
    ControlField = 11
    BookmarkStart = 12
    BookmarkEnd = 13
    PermissionStart = 14
    PermissionEnd = 15
    ShapeObject = 16
    ShapeGroup = 17
    Comment = 18
    CommentMark = 19
    Footnote = 20
    TextBox = 21
    Break = 22
    Symbol = 23
    TOC = 24
    OleObject = 25
