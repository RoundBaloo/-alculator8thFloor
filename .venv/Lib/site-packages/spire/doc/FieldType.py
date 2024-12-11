from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FieldType(Enum):
    """
    Enum class representing the type of fields.
    """
    FieldNone = 0
    FieldAddin = 81
    FieldAdvance = 84
    FieldAsk = 38
    FieldAuthor = 17
    FieldAutoNum = 54
    FieldAutoNumLegal = 53
    FieldAutoNumOutline = 52
    FieldAutoText = 79
    FieldAutoTextList = 89
    FieldBarcode = 63
    FieldCitation = 1980
    FieldComments = 19
    FieldCompare = 80
    FieldCreateDate = 21
    FieldData = 40
    FieldDatabase = 78
    FieldDate = 31
    FieldDDE = 45
    FieldDDEAuto = 46
    FieldDocProperty = 85
    FieldDocVariable = 64
    FieldEditTime = 25
    FieldEmbed = 58
    FieldEmpty = -1
    FieldFormula = 34
    FieldExpression = 34
    FieldFileName = 29
    FieldFileSize = 69
    FieldFillIn = 39
    FieldFootnoteRef = 5
    FieldFormCheckBox = 71
    FieldFormDropDown = 83
    FieldFormTextInput = 70
    FieldEquation = 49
    FieldGlossary = 47
    FieldGoToButton = 50
    FieldHTMLActiveX = 91
    FieldHyperlink = 88
    FieldIf = 7
    FieldImport = 55
    FieldInclude = 36
    FieldIncludePicture = 67
    FieldIncludeText = 68
    FieldIndex = 8
    FieldIndexEntry = 4
    FieldInfo = 14
    FieldKeyWord = 18
    FieldLastSavedBy = 20
    FieldLink = 56
    FieldListNum = 90
    FieldMacroButton = 51
    FieldMergeField = 59
    FieldMergeRec = 44
    FieldMergeSeq = 75
    FieldNext = 41
    FieldNextIf = 42
    FieldNoteRef = 72
    FieldNumChars = 28
    FieldNumPages = 26
    FieldNumWords = 27
    FieldOCX = 87
    FieldPage = 33
    FieldPageRef = 37
    FieldPrint = 48
    FieldPrintDate = 23
    FieldPrivate = 77
    FieldQuote = 35
    FieldRef = 3
    FieldRefDoc = 11
    FieldRevisionNum = 24
    FieldSaveDate = 22
    FieldSection = 65
    FieldSectionPages = 66
    FieldSequence = 12
    FieldSet = 6
    FieldSkipIf = 43
    FieldStyleRef = 10
    FieldSubject = 16
    FieldSubscriber = 82
    FieldSymbol = 57
    FieldTemplate = 30
    FieldTime = 32
    FieldTitle = 15
    FieldTOA = 73
    FieldTOAEntry = 74
    FieldTOC = 13
    FieldTOCEntry = 9
    FieldUserAddress = 62
    FieldUserInitials = 61
    FieldUserName = 60
    FieldShape = 95
    FieldBidiOutline = 92
    FieldAddressBlock = 93
    FieldUnknown = 1000
    FieldCannotParse = 1
    FieldGreetingLine = 94
    FieldRefNoKeyword = 2
    FieldMacro = 76
    FieldMergeBarcode = 6302
    FieldDisplayBarcode = 6301
    FieldBibliography = 100500
