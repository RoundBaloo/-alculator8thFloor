from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class EditingGroup(Enum):
    """
    Enum class representing the set of possible aliases (or editing groups) which can be used as aliases to determine if the current user shall be allowed to edit a single range defined by a range permission within a document. This mechanism provides a set of predefined editing groups which can be associated with accounts by applications in any desired manner.

    """
    none = 0
    Current = 65530
    Editors = 65531
    Owners = 65532
    Contributors = 65533
    Administrators = 65534
    Everyone = 65535
