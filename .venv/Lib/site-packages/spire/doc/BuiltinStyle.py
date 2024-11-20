from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BuiltinStyle(Enum):
    """
    Enum class that defines built-in styles.
    """

    Normal = 0
    Heading1 = 1
    Heading2 = 2
    Heading3 = 3
    Heading4 = 4
    Heading5 = 5
    Heading6 = 6
    Heading7 = 7
    Heading8 = 8
    Heading9 = 9
    Index1 = 10
    Index2 = 11
    Index3 = 12
    Index4 = 13
    Index5 = 14
    Index6 = 15
    Index7 = 16
    Index8 = 17
    Index9 = 18
    Toc1 = 19
    Toc2 = 20
    Toc3 = 21
    Toc4 = 22
    Toc5 = 23
    Toc6 = 24
    Toc7 = 25
    Toc8 = 26
    Toc9 = 27
    NormalIndent = 28
    FootnoteText = 29
    CommentText = 30
    Header = 31
    Footer = 32
    IndexHeading = 33
    Caption = 34
    TableOfFigures = 35
    FootnoteReference = 38
    CommentReference = 39
    LineNumber = 40
    PageNumber = 41
    EndnoteReference = 42
    EndnoteText = 43
    TableOfAuthorities = 44
    MacroText = 45
    ToaHeading = 46
    List = 47
    ListBullet = 48
    ListNumber = 49
    List2 = 50
    List3 = 51
    List4 = 52
    List5 = 53
    ListBullet2 = 54
    ListBullet3 = 55
    ListBullet4 = 56
    ListBullet5 = 57
    ListNumber2 = 58
    ListNumber3 = 59
    ListNumber4 = 60
    ListNumber5 = 61
    Title = 62
    Closing = 63
    Signature = 64
    DefaultParagraphFont = 65
    BodyText = 66
    BodyTextInd = 67
    ListContinue = 68
    ListContinue2 = 69
    ListContinue3 = 70
    ListContinue4 = 71
    ListContinue5 = 72
    MessageHeader = 73
    Subtitle = 74
    Salutation = 75
    Date = 76
    BodyText1I = 77
    BodyText1I2 = 78
    NoteHeading = 79
    BodyText2 = 80
    BodyText3 = 81
    BodyTextInd2 = 82
    BodyTextInd3 = 83
    BlockText = 84
    Hyperlink = 85
    FollowedHyperlink = 86
    Strong = 87
    Emphasis = 88
    DocumentMap = 89
    PlainText = 90
    EmailSignature = 91
    NormalWeb = 94
    HtmlAcronym = 95
    HtmlAddress = 96
    HtmlCite = 97
    HtmlCode = 98
    HtmlDefinition = 99
    HtmlKeyboard = 100
    HtmlPreformatted = 101
    HtmlSample = 102
    HtmlTypewriter = 103
    HtmlVariable = 104
    CommentSubject = 106
    NoList = 107
    BalloonText = 153
    User = 4094
    NoStyle = 4095
