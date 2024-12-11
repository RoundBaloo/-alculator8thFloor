from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IParagraph (  IBodyRegion, IStyleHolder, ICompositeObject) :
    """
    Represents a paragraph in a document.
    """
    @property

    @abc.abstractmethod
    def Text(self)->str:
        """
        Gets or sets the text content of the paragraph.
        """
        pass


    @Text.setter
    @abc.abstractmethod
    def Text(self, value:str):
        """
        Sets the text content of the paragraph.
        """
        pass



    @abc.abstractmethod
    def get_Item(self ,index:int)->'ParagraphBase':
        """
        Gets the paragraph item at the specified index.
        """
        pass


    @property

    @abc.abstractmethod
    def Items(self)->'ParagraphItemCollection':
        """
        Gets the collection of paragraph items in the paragraph.
        """
        pass


    @property

    @abc.abstractmethod
    def Format(self)->'ParagraphFormat':
        """
        Gets the formatting settings for the paragraph.
        """
        pass


    @property

    @abc.abstractmethod
    def ListFormat(self)->'ListFormat':
        """
        Gets the list formatting settings for the paragraph.
        """
        pass


    @property

    @abc.abstractmethod
    def BreakCharacterFormat(self)->'CharacterFormat':
        """
        Gets the character formatting settings for the break character in the paragraph.
        """
        pass


    @property
    @abc.abstractmethod
    def IsInCell(self)->bool:
        """
        Gets a value indicating whether the paragraph is inside a table cell.
        """
        pass


    @property
    @abc.abstractmethod
    def IsEndOfSection(self)->bool:
        """
        Gets a value indicating whether the paragraph is at the end of a section.
        """
        pass


    @property
    @abc.abstractmethod
    def IsEndOfDocument(self)->bool:
        """
        Gets a value indicating whether the paragraph is at the end of the document.
        """
        pass



    @abc.abstractmethod
    def AppendText(self ,text:str)->'TextRange':
        """
        Appends the specified text to the paragraph and returns the appended text range.
        """
        pass


#
#    @abc.abstractmethod
#    def AppendPicture(self ,imageBytes:'Byte[]')->'DocPicture':
#        """
#
#        """
#        pass
#



    @abc.abstractmethod
    def AppendField(self ,fieldName:str,fieldType:'FieldType')->'Field':
        """
        Appends a field with the specified name and type to the paragraph and returns the appended field.
        """
        pass



    @abc.abstractmethod
    def AppendBookmarkStart(self ,name:str)->'BookmarkStart':
        """
        Appends a bookmark start with the specified name to the paragraph and returns the appended bookmark start.
        """
        pass



    @abc.abstractmethod
    def AppendBookmarkEnd(self ,name:str)->'BookmarkEnd':
        """
        Appends a bookmark end with the specified name to the paragraph and returns the appended bookmark end.
        """
        pass



    @abc.abstractmethod
    def AppendComment(self ,text:str)->'Comment':
        """
        Appends a comment with the specified text to the paragraph and returns the appended comment.
        """
        pass



    @abc.abstractmethod
    def AppendFootnote(self ,type:'FootnoteType')->'Footnote':
        """
        Appends a footnote with the specified type to the paragraph and returns the appended footnote.
        """
        pass



    @abc.abstractmethod
    def AppendTextBox(self ,width:float,height:float)->'TextBox':
        """
        Appends a text box with the specified width and height to the paragraph and returns the appended text box.
        """
        pass



    @abc.abstractmethod
    def AppendSymbol(self ,characterCode:int)->'Symbol':
        """
        Appends a symbol with the specified character code to the paragraph and returns the appended symbol.
        """
        pass



    @abc.abstractmethod
    def AppendBreak(self ,breakType:'BreakType')->'Break':
        """
        Appends a break with the specified type to the paragraph and returns the appended break.
        """
        pass



    @abc.abstractmethod
    def AppendHTML(self ,html:str):
        """
        Appends the specified HTML content to the paragraph.
        """
        pass



    @abc.abstractmethod
    def GetStyle(self)->'ParagraphStyle':
        """
        Gets the style applied to the paragraph.
        """
        pass



    @abc.abstractmethod
    def Replace(self ,given:str,textSelection:'TextSelection',caseSensitive:bool,wholeWord:bool)->int:
        """
        Replaces the specified text in the paragraph with the specified replacement text and returns the number of replacements made.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendCheckBox(self)->'CheckBoxFormField':
        """
        Appends a checkbox form field to the paragraph and returns the appended checkbox form field.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendTextFormField(self ,defaultText:str)->'TextFormField':
        """
        Appends a text form field with the specified default text to the paragraph and returns the appended text form field.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendDropDownFormField(self)->'DropDownFormField':
        """
        Appends a dropdown form field to the paragraph and returns the appended dropdown form field.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendCheckBox(self ,checkBoxName:str,defaultCheckBoxValue:bool)->'CheckBoxFormField':
        """
        Appends a checkbox form field with the specified name and default value to the paragraph and returns the appended checkbox form field.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendTextFormField(self ,formFieldName:str,defaultText:str)->'TextFormField':
        """
        Appends a text form field with the specified name and default text to the paragraph and returns the appended text form field.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendDropDownFormField(self ,dropDropDownName:str)->'DropDownFormField':
        """
        Appends a dropdown form field with the specified name to the paragraph and returns the appended dropdown form field.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendHyperlink(self ,link:str,text:str,type:HyperlinkType)->'Field':
        """
        Appends a hyperlink with the specified link, display text, and type to the paragraph and returns the appended hyperlink field.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendHyperlink(self ,link:str,picture:'DocPicture',type:HyperlinkType)->'Field':
        """
        Appends a hyperlink with the specified link, picture, and type to the paragraph and returns the appended hyperlink field.
        """
        pass


    @abc.abstractmethod
    def RemoveAbsPosition(self):
        """
        Removes the absolute position of the paragraph.
        """
        pass



    @abc.abstractmethod
    def AppendTOC(self ,lowerHeadingLevel:int,upperHeadingLevel:int)->'TableOfContent':
        """
        Appends a table of contents with the specified lower and upper heading levels to the paragraph and returns the appended table of contents.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendOleObject(self ,oleStream:Stream,olePicture:'DocPicture',type:OleObjectType)->'DocOleObject':
        """
        Appends an OLE object with the specified stream, picture, and type to the paragraph and returns the appended OLE object.
        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def AppendOleObject(self ,oleBytes:'Byte[]',olePicture:DocPicture,type:OleObjectType)->DocOleObject:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def AppendOleObject(self ,pathToFile:str,olePicture:'DocPicture',type:OleObjectType)->'DocOleObject':
        """
        Appends an OLE object with the specified file path, picture, and type to the paragraph and returns the appended OLE object.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendOleObject(self ,pathToFile:str,olePicture:'DocPicture')->'DocOleObject':
        """

        """
        pass


    @dispatch

    @abc.abstractmethod
    def AppendOleObject(self ,stream:Stream,pic:'DocPicture',oleLinkType:OleLinkType)->'DocOleObject':
        """
        Appends an OLE object with the specified stream, picture, and link type to the paragraph and returns the appended OLE object.
        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def AppendOleObject(self ,oleBytes:'Byte[]',olePicture:DocPicture,oleLinkType:OleLinkType)->DocOleObject:
#        """
#
#        """
#        pass
#


#    @dispatch
#
#    @abc.abstractmethod
#    def AppendOleObject(self ,oleBytes:'Byte[]',olePicture:DocPicture,fileExtension:str)->DocOleObject:
#        """
#
#        """
#        pass
#


    @dispatch

    @abc.abstractmethod
    def AppendOleObject(self ,oleStream:Stream,olePicture:'DocPicture',fileExtension:str)->'DocOleObject':
        """
        Appends an OLE object with the specified stream, picture, and file extension to the paragraph and returns the appended OLE object.
        """
        pass


