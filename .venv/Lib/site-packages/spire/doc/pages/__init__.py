import sys
from ctypes import *
from spire.doc.common import *

from spire.doc.common.Common import IntPtrArray
from spire.doc.common.Common import IntPtrWithTypeName

from spire.doc.common.SpireObject import SpireObject
from spire.doc.common.RectangleF import RectangleF

from spire.doc.pages.LayoutElement import LayoutElement
from spire.doc.pages.BodyLayoutElement import BodyLayoutElement
from spire.doc.pages.FixedLayoutCell import FixedLayoutCell
from spire.doc.pages.FixedLayoutColumn import FixedLayoutColumn
from spire.doc.pages.FixedLayoutComment import FixedLayoutComment
from spire.doc.pages.FixedLayoutDocument import FixedLayoutDocument
from spire.doc.pages.FixedLayoutEndnote import FixedLayoutEndnote
from spire.doc.pages.FixedLayoutFootnote import FixedLayoutFootnote
from spire.doc.pages.FixedLayoutHeaderFooter import FixedLayoutHeaderFooter
from spire.doc.pages.FixedLayoutLine import FixedLayoutLine
from spire.doc.pages.FixedLayoutNoteSeparator import FixedLayoutNoteSeparator
from spire.doc.pages.FixedLayoutPage import FixedLayoutPage
from spire.doc.pages.FixedLayoutRow import FixedLayoutRow
from spire.doc.pages.FixedLayoutSpan import FixedLayoutSpan
from spire.doc.pages.FixedLayoutTextBox import FixedLayoutTextBox
from spire.doc.pages.LayoutCollection import LayoutCollection
from spire.doc.pages.LayoutFixedLCellCollection import LayoutFixedLCellCollection
from spire.doc.pages.LayoutFixedLColumnCollection import LayoutFixedLColumnCollection
from spire.doc.pages.LayoutFixedLCommentCollection import LayoutFixedLCommentCollection
from spire.doc.pages.LayoutFixedLDocumentCollection import LayoutFixedLDocumentCollection
from spire.doc.pages.LayoutFixedLEndnoteCollection import LayoutFixedLEndnoteCollection
from spire.doc.pages.LayoutFixedLFootnoteCollection import LayoutFixedLFootnoteCollection
from spire.doc.pages.LayoutFixedLHeaderFooterCollection import LayoutFixedLHeaderFooterCollection
from spire.doc.pages.LayoutFixedLLineCollection import LayoutFixedLLineCollection
from spire.doc.pages.LayoutFixedLNoteSeparatorCollection import LayoutFixedLNoteSeparatorCollection
from spire.doc.pages.LayoutFixedLPagesCollection import LayoutFixedLPagesCollection
from spire.doc.pages.LayoutFixedLRowCollection import LayoutFixedLRowCollection
from spire.doc.pages.LayoutFixedLSpanCollection import LayoutFixedLSpanCollection
from spire.doc.pages.LayoutFixedLTextBoxCollection import LayoutFixedLTextBoxCollection
from spire.doc.pages.LayoutElementType import LayoutElementType