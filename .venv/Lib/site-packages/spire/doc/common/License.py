from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
if __package__ == "spire.pdf.common":
    from spire.pdf.common import *
elif __package__ == "spire.xls.common":
    from spire.xls.common import *
elif __package__ == "spire.doc.common":
    from spire.doc.common import *
else :
    from spire.presentation.common import *
#from spire.xls import *
from ctypes import *
import abc

class License (SpireObject) :
    """

    """
    @staticmethod
    def SetLicenseFileFullPathByDLLHander(dllhander, licenseFileFullPath:str):
        if __package__ == "spire.doc.common" or __package__ == "spire.presentation.common":
            licenseFileFullPathPtr = StrToPtr(licenseFileFullPath)
            if dllhander != None:
                dllhander.LISetLicenseFileFullPath.argtypes=[ c_char_p]
                dllhander.LISetLicenseFileFullPath( licenseFileFullPathPtr)
        else:
            if dllhander != None:
                dllhander.LISetLicenseFileFullPath.argtypes=[ c_wchar_p]
                dllhander.LISetLicenseFileFullPath( licenseFileFullPath)
        
    @staticmethod
    def SetLicenseFileFullPath(licenseFileFullPath:str):
        """
        <summary>
            Provides a license by a license file path, which will be used for loading license.
        </summary>
		<param name="licenseFileFullPath">License file full path.</param>
        """
        if __package__ == "spire.doc.common" or __package__ == "spire.presentation.common":
            licenseFileFullPathPtr = StrToPtr(licenseFileFullPath)
            License.SetLicenseFileFullPathByDLLHander(GetDllLibDoc(), licenseFileFullPathPtr)
            License.SetLicenseFileFullPathByDLLHander(GetDllLibPdf(), licenseFileFullPathPtr)
            License.SetLicenseFileFullPathByDLLHander(GetDllLibXls(), licenseFileFullPathPtr)
            License.SetLicenseFileFullPathByDLLHander(GetDllLibPpt(), licenseFileFullPathPtr)
        else:
            License.SetLicenseFileFullPathByDLLHander(GetDllLibDoc(), licenseFileFullPath)
            License.SetLicenseFileFullPathByDLLHander(GetDllLibPdf(), licenseFileFullPath)
            License.SetLicenseFileFullPathByDLLHander(GetDllLibXls(), licenseFileFullPath)
            License.SetLicenseFileFullPathByDLLHander(GetDllLibPpt(), licenseFileFullPath)
        

    @staticmethod
    def SetLicenseFileName(licenseFileName:str):
        """
		<summary>
		    Gets the current license file name.
		</summary>
		<returns>The license file name, the default license file name is [license.elic.xml].</returns>
        """
        if __package__ == "spire.doc.common" or __package__ == "spire.presentation.common":
            licenseFileNamePtr = StrToPtr(licenseFileName)
            License.SetLicenseFileNameByDLLHander(GetDllLibDoc(), licenseFileNamePtr)
            License.SetLicenseFileNameByDLLHander(GetDllLibPdf(), licenseFileNamePtr)
            License.SetLicenseFileNameByDLLHander(GetDllLibXls(), licenseFileNamePtr)
            License.SetLicenseFileNameByDLLHander(GetDllLibPpt(), licenseFileNamePtr)
        else:
            License.SetLicenseFileNameByDLLHander(GetDllLibDoc(), licenseFileName)
            License.SetLicenseFileNameByDLLHander(GetDllLibPdf(), licenseFileName)
            License.SetLicenseFileNameByDLLHander(GetDllLibXls(), licenseFileName)
            License.SetLicenseFileNameByDLLHander(GetDllLibPpt(), licenseFileName)
        
    @staticmethod
    def SetLicenseFileNameByDLLHander(dllhander, licenseFileName:str):
        if __package__ == "spire.doc.common" or __package__ == "spire.presentation.common":
            licenseFileNamePtr = StrToPtr(licenseFileName)
            if dllhander != None:
                dllhander.LISetLicenseFileName.argtypes=[ c_char_p]
                dllhander.LISetLicenseFileName(licenseFileNamePtr)
        else:
            if dllhander != None:
                dllhander.LISetLicenseFileName.argtypes=[ c_wchar_p]
                dllhander.LISetLicenseFileName( licenseFileName)
        

    @staticmethod
    def SetLicenseFileStream(stream:Stream):
        """
		<summary>
    		Provides a license by a license stream, which will be used for loading license.
		</summary>
		<param name="licenseFileStream">License data stream.</param>
        """
        License.SetLicenseFileStreamByDLLHander(GetDllLibDoc(), stream)
        License.SetLicenseFileStreamByDLLHander(GetDllLibPdf(), stream)
        License.SetLicenseFileStreamByDLLHander(GetDllLibXls(), stream)
        License.SetLicenseFileStreamByDLLHander(GetDllLibPpt(), stream)
    @staticmethod
    def SetLicenseFileStreamByDLLHander(dllhander, stream:Stream):
        if dllhander != None:
            intPtrobj:c_void_p = stream.Ptr
            dllhander.LISetLicenseFileStream.argtypes=[ c_void_p]
            dllhander.LISetLicenseFileStream( intPtrobj)

    @staticmethod
    def SetLicenseKey(key:str):
        """
		<summary>    
    		Provides a license by a license key, which will be used for loading license.
		</summary>
		<param name="key">The value of the Key attribute of the element License of you license xml file.</param> 
        """
        if __package__ == "spire.doc.common" or __package__ == "spire.presentation.common":
            keyStr = StrToPtr(key)
            License.SetLicenseKeyByDLLHander(GetDllLibDoc(), keyStr)
            License.SetLicenseKeyByDLLHander(GetDllLibPdf(), keyStr)
            License.SetLicenseKeyByDLLHander(GetDllLibXls(), keyStr)
            License.SetLicenseKeyByDLLHander(GetDllLibPpt(), keyStr)
        else:
            License.SetLicenseKeyByDLLHander(GetDllLibDoc(), key)
            License.SetLicenseKeyByDLLHander(GetDllLibPdf(), key)
            License.SetLicenseKeyByDLLHander(GetDllLibXls(), key)
            License.SetLicenseKeyByDLLHander(GetDllLibPpt(), key)
        
    @staticmethod
    def SetLicenseKeyByDLLHander(dllhander, key:str):
        if __package__ == "spire.doc.common" or __package__ == "spire.presentation.common":
            keyPtr = StrToPtr(key)
            if dllhander != None:
                dllhander.LISetLicenseKey.argtypes=[ c_char_p]
                dllhander.LISetLicenseKey(keyPtr)
        else:
            if dllhander != None:
                dllhander.LISetLicenseKey.argtypes=[ c_wchar_p]
                dllhander.LISetLicenseKey( key)
        

    @staticmethod
    def ClearLicense():
        """
		<summary>
		    Clear all cached license.
		</summary>
        """
        License.ClearLicenseByDLLHander(GetDllLibDoc())
        License.ClearLicenseByDLLHander(GetDllLibPdf())
        License.ClearLicenseByDLLHander(GetDllLibXls())
        License.ClearLicenseByDLLHander(GetDllLibPpt())
    @staticmethod
    def ClearLicenseByDLLHander(dllhander):
        if dllhander != None:
            dllhander.LIClearLicense( )

    @staticmethod
    def GetLicenseFileName()->str:
        """
		<summary>
		    Gets the current license file name.
		</summary>
		<returns>The license file name, the default license file name is [license.elic.xml].</returns>
        """
        ret = License.GetLicenseFileNameByDLLHander(GetDllLibDoc())
        if ret == None:
            ret = License.GetLicenseFileNameByDLLHander(GetDllLibPdf())
        if ret == None:
            ret = License.GetLicenseFileNameByDLLHander(GetDllLibXls())
        if ret == None:
            ret = License.GetLicenseFileNameByDLLHander(GetDllLibPpt())
        return ret
    @staticmethod
    def GetLicenseFileNameByDLLHander(dllhander)->str:
        if dllhander != None:
            dllhander.LIGetLicenseFileName.argtypes=[c_void_p]
            return dllhander.LIGetLicenseFileName( )
        return None