from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BuiltInProperty(Enum):
    """
    Enum class representing built-in properties in a document.
    """

    Title = 2
    Subject = 3
    Author = 4
    Keywords = 5
    Comments = 6
    Template = 7
    LastAuthor = 8
    RevisionNumber = 9
    EditTime = 10
    LastPrinted = 11
    CreationDate = 12
    LastSaveDate = 13
    PageCount = 14
    WordCount = 15
    CharCount = 16
    Thumbnail = 17
    ApplicationName = 18
    Security = 19
    Category = 1000
    PresentationTarget = 1001
    ByteCount = 1002
    LineCount = 1003
    ParagraphCount = 1004
    SlideCount = 1005
    NoteCount = 1006
    HiddenCount = 1007
    MultimediaClipCount = 1008
    ScaleCrop = 1009
    HeadingPair = 1010
    DocParts = 1011
    Manager = 1012
    Company = 1013
    LinksDirty = 1014
    CharactersWithSpaces = 1015
    ShareDoc = 1016
    LinkBase = 1017
    Hyperlinks = 1018
    HyperlinksChanged = 1019
    Version = 1020
    ExcelDigitalSignature = 1021
    ContentType = 1022
    ContentStatus = 1023
    Language = 1024
    DocVersion = 1025
