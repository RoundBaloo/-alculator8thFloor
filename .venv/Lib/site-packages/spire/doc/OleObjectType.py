from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class OleObjectType(Enum):
    """
    Enum class that defines the types of OLE object.
    """
    Undefined = 0
    AdobeAcrobatDocument = 1
    BitmapImage = 2
    MediaClip = 3
    Equation = 4
    GraphChart = 5
    Excel_97_2003_Worksheet = 6
    ExcelBinaryWorksheet = 7
    ExcelChart = 8
    ExcelMacroWorksheet = 9
    ExcelWorksheet = 10
    PowerPoint_97_2003_Presentation = 11
    PowerPoint_97_2003_Slide = 12
    PowerPointMacroPresentation = 13
    PowerPointMacroSlide = 14
    PowerPointPresentation = 15
    PowerPointSlide = 16
    Word_97_2003_Document = 17
    WordDocument = 18
    WordMacroDocument = 19
    VisioDrawing = 20
    MIDISequence = 21
    OpenDocumentPresentation = 22
    OpenDocumentSpreadsheet = 23
    OpenDocumentText = 24
    OpenOfficeSpreadsheet1_1 = 25
    OpenOfficeText_1_1 = 26
    Package = 27
    VideoClip = 28
    WaveSound = 29
    WordPadDocument = 30
    OpenOfficeSpreadsheet = 31
    OpenOfficeText = 32
    VisioDrawing_2013 = 33
    WordPicture = 34
    MathType = 35
    WordTemplate = 36
    WordMacroTemplate = 37
