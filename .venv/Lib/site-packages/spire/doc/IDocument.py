from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IDocument (  ICompositeObject, IDocumentObject) :
    """
    Interface for a document object.
    """
    @property

    @abc.abstractmethod
    def BuiltinDocumentProperties(self)->'BuiltinDocumentProperties':
        """
        Returns the built-in document properties.
        """
        pass


    @property

    @abc.abstractmethod
    def CustomDocumentProperties(self)->'CustomDocumentProperties':
        """
        Returns the custom document properties.
        """
        pass


    @property

    @abc.abstractmethod
    def Sections(self)->'SectionCollection':
        """
        Returns the collection of sections in the document.
        """
        pass


    @property

    @abc.abstractmethod
    def Styles(self)->'StyleCollection':
        """
        Returns the collection of styles in the document.
        """
        pass


    @property

    @abc.abstractmethod
    def ListStyles(self)->'ListStyleCollection':
        """
        Returns the collection of list styles in the document.
        """
        pass


    @property

    @abc.abstractmethod
    def Bookmarks(self)->'BookmarkCollection':
        """
        Returns the collection of bookmarks in the document.
        """
        pass


    @property

    @abc.abstractmethod
    def TextBoxes(self)->'TextBoxCollection':
        """
        Returns the collection of text boxes in the document.
        """
        pass


    @property

    @abc.abstractmethod
    def TOC(self)->'TableOfContent':
        """
        Returns the table of contents in the document.
        """
        pass


    @TOC.setter
    @abc.abstractmethod
    def TOC(self, value:'TableOfContent'):
        """
        Sets the table of contents in the document.
        """
        pass


    @property

    @abc.abstractmethod
    def Comments(self)->'CommentsCollection':
        """
        Returns the collection of comments in the document.
        """
        pass


    @property

    @abc.abstractmethod
    def LastSection(self)->'Section':
        """
        Returns the last section in the document.
        """
        pass


    @property

    @abc.abstractmethod
    def LastParagraph(self)->'Paragraph':
        """
        Returns the last paragraph in the document.
        """
        pass


    @abc.abstractmethod
    def GetProtectionType(self)->'ProtectionType':
        """
        Returns the protection type of the document.
        """
        pass


    @abc.abstractmethod
    def SetProtectionType(self, value:'ProtectionType'):
        """
        Sets the protection type of the document.
        """
        pass


    @property

    @abc.abstractmethod
    def ViewSetup(self)->'ViewSetup':
        """
        Returns the view setup of the document.
        """
        pass


    @property

    @abc.abstractmethod
    def Watermark(self)->'WatermarkBase':
        """
        Returns the watermark of the document.
        """
        pass


    @Watermark.setter
    @abc.abstractmethod
    def Watermark(self, value:'WatermarkBase'):
        """
        Sets the watermark of the document.
        """
        pass


    @property

    @abc.abstractmethod
    def MailMerge(self)->'MailMerge':
        """
        Returns the mail merge object of the document.
        """
        pass


    @property

    @abc.abstractmethod
    def Background(self)->'Background':
        """
        Returns the background of the document.
        """
        pass


    @property

    @abc.abstractmethod
    def Variables(self)->'VariableCollection':
        """
        Returns the collection of variables in the document.
        """
        pass


    @property

    @abc.abstractmethod
    def Properties(self)->'DocumentProperties':
        """
        Returns the properties of the document.
        """
        pass


    @property
    @abc.abstractmethod
    def HasChanges(self)->bool:
        """
        Returns True if the document has changes, False otherwise.
        """
        pass


    @property
    @abc.abstractmethod
    def IsUpdateFields(self)->bool:
        """
        Returns True if the document is set to update fields, False otherwise.
        """
        pass


    @IsUpdateFields.setter
    @abc.abstractmethod
    def IsUpdateFields(self, value:bool):
        """
        Sets whether the document should update fields or not.
        """
        pass


    @abc.abstractmethod
    def CreateMinialDocument(self):
        """
        Creates a minimal document.
        """
        pass



    @abc.abstractmethod
    def AddSection(self)->'Section':
        """
        Adds a new section to the document and returns it.
        """
        pass



    @abc.abstractmethod
    def AddParagraphStyle(self ,styleName:str)->'ParagraphStyle':
        """
        Adds a new paragraph style to the document and returns it.
        """
        pass



    @abc.abstractmethod
    def AddListStyle(self ,listType:'ListType',styleName:str)->'ListStyle':
        """
        Adds a new list style to the document and returns it.
        """
        pass



    @abc.abstractmethod
    def GetText(self)->str:
        """
        Returns the text content of the document.
        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def SaveToImages(self ,type:ImageType)->List[SKImage]:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def SaveToImages(self ,pageIndex:int,type:ImageType)->SKImage:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def SaveToImages(self ,pageIndex:int,noOfPages:int,type:ImageType)->List[SKImage]:
#        """
#
#        """
#        pass
#



    @abc.abstractmethod
    def CreateParagraph(self)->'Paragraph':
        """
        Creates a new paragraph in the document and returns it.
        """
        pass



    @abc.abstractmethod
    def Clone(self)->'Document':
        """
        Creates a clone of the document and returns it.
        """
        pass



    @abc.abstractmethod
    def AddStyle(self ,builtinStyle:'BuiltinStyle')->'Style':
        """
        Adds a new style to the document and returns it.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def Protect(self ,type:ProtectionType):
        """
        Protects the document with the specified protection type.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def Protect(self ,type:ProtectionType,password:str):
        """
        Protects the document with the specified protection type and password.
        """
        pass



    @abc.abstractmethod
    def Encrypt(self ,password:str):
        """
        Encrypts the document with the specified password.
        """
        pass


    @abc.abstractmethod
    def RemoveEncryption(self):
        """
        Removes the encryption from the document.
        """
        pass


    @abc.abstractmethod
    def UpdateWordCount(self):
        """
        Updates the word count of the document.
        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def FindPattern(self ,pattern:'Regex')->TextSelection:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def FindString(self ,given:str,caseSensitive:bool,wholeWord:bool)->TextSelection:
        """
        Finds the given string in the document and returns the text selection.
        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def FindPatternInLine(self ,pattern:'Regex')->List[TextSelection]:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def FindStringInLine(self ,given:str,caseSensitive:bool,wholeWord:bool)->List[TextSelection]:
#        """
#
#        """
#        pass
#


#
#    @abc.abstractmethod
#    def FindAllPattern(self ,pattern:'Regex')->List['TextSelection']:
#        """
#
#        """
#        pass
#


#
#    @abc.abstractmethod
#    def FindAllString(self ,given:str,caseSensitive:bool,wholeWord:bool)->List['TextSelection']:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def Replace(self ,pattern:'Regex',replace:str)->int:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def Replace(self ,given:str,replace:str,caseSensitive:bool,wholeWord:bool)->int:
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def Replace(self ,pattern:'Regex',textSelection:TextSelection)->int:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def Replace(self ,given:str,textSelection:TextSelection,caseSensitive:bool,wholeWord:bool)->int:
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def ReplaceInLine(self ,given:str,replace:str,caseSensitive:bool,wholeWord:bool)->int:
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def ReplaceInLine(self ,pattern:'Regex',replace:str)->int:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def ReplaceInLine(self ,given:str,replacement:TextSelection,caseSensitive:bool,wholeWord:bool)->int:
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def ReplaceInLine(self ,pattern:'Regex',replacement:TextSelection)->int:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def FindString(self ,startTextBodyItem:BodyRegion,given:str,caseSensitive:bool,wholeWord:bool)->TextSelection:
        """

        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def FindPattern(self ,startBodyItem:BodyRegion,pattern:'Regex')->TextSelection:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def FindStringInLine(self ,startTextBodyItem:BodyRegion,given:str,caseSensitive:bool,wholeWord:bool)->List[TextSelection]:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def FindPatternInLine(self ,startBodyItem:BodyRegion,pattern:'Regex')->List[TextSelection]:
#        """
#
#        """
#        pass
#


    @abc.abstractmethod
    def ResetFindState(self):
        """
        Resets the find state of the document.
        """
        pass



    @abc.abstractmethod
    def LoadFromStream(self ,stream:'Stream',fileFormat:'FileFormat'):
        """
        Loads the document from the specified stream with the specified file format.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def SaveToFile(self ,stream:Stream,fileFormat:FileFormat):
        """
        Saves the document to the specified stream with the specified file format.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def LoadFromFile(self ,fileName:str):
        """
        Loads the document from the specified file.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def LoadFromFile(self ,fileName:str,fileFormat:FileFormat):
        """
        Loads the document from the specified file with the specified file format.
        """
        pass



    @abc.abstractmethod
    def LoadFromFileInReadMode(self ,strFileName:str,fileFormat:'FileFormat'):
        """
        Loads the document from the specified file in read mode with the specified file format.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def SaveToFile(self ,fileName:str):
        """
        Saves the document to the specified file.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def SaveToFile(self ,fileName:str,fileFormat:FileFormat):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def ImportContent(self ,doc:'IDocument'):
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def ImportContent(self ,doc:'IDocument',importStyles:bool):
        """

        """
        pass


