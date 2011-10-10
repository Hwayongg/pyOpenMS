import unittest
import pyOpenMS as p
from   nose.tools import *

class TestBasisObjects(unittest.TestCase):


    def test_Spectrum(self):

        """
        @tests:
        MSSpectrum.__init__
        .size
        .getRT
        .setRT
        .getMSLevel
        .setMSLevel
        .getPrecursors
        .setPrecursors
        .clear
        .push_back

        Precursor.getMZ
        .setMZ
        .setIntensity
        .setIntensity

        Peak1D.__init__
        .setMZ
        .getMZ
        .setIntensity
        .getIntensity
                          
        @end 
        """
        spec = p.MSSpectrum()
        assert  spec.size() == 0

        spec.setRT(1.0)
        assert abs(spec.getRT()-1.0) < 1e-5

        spec.setMSLevel(3)
        assert spec.getMSLevel() == 3

        ex = None
        try:
            spec.setMSLevel(-1)
        except Exception ,e:
            ex = e
        assert ex is not None

        pc0 = p.Precursor()
        pc0.setMZ(16.0)
        pc0.setIntensity(256.0)

        pc1 = p.Precursor()
        pc1.setMZ(32.0)
        pc1.setIntensity(128.0)
        
        spec.setPrecursors([pc0, pc1])

        pcs = spec.getPrecursors()
        print pcs
        eq_(len(pcs), 2)
        assert pcs[0].getMZ() == pc0.getMZ()
        assert pcs[1].getMZ() == pc1.getMZ()
        assert pcs[0].getIntensity() == pc0.getIntensity()
        assert pcs[1].getIntensity() == pc1.getIntensity()

        peak = p.Peak1D()
        peak.setMZ(1.25)
        peak.setIntensity(123.0)

        spec = p.MSSpectrum()
        spec.push_back(peak)
        assert spec.size() == 1
        assert spec[0].getMZ() == 1.25
        assert spec[0].getIntensity() == 123.0

        spec.clear(False)
        assert spec.size() == 0
        



    def test_Peak1D(self):
        """
        @tests:
        Peak1D.__init__
              .setMZ
              .getMZ
              .setIntensity
              .getIntensity
        """
        peak = p.Peak1D()

        peak.setMZ(1.0)
        assert abs(peak.getMZ()-1.0) < 1e-5

        peak.setIntensity(4.0)
        assert abs(peak.getIntensity()-4.0) < 1e-5

    def test_Precursor(self):
        """
        @tests:
        Precursor.__init__
                 .setMZ
                 .getMZ
                 .setIntensity
                 .getIntensity
        """
        pc = p.Precursor()

        pc.setMZ(1.0)
        assert abs(pc.getMZ()-1.0) < 1e-5

        pc.setIntensity(4.0)
        assert abs(pc.getIntensity()-4.0) < 1e-5

    def test_InstrumentSettings(self):
        """
        @tests:
        InstrumentSettings.__init__
        .getPolarity
        .setPolarity
        Polarity.POLNULL
        Polarity.POSITIVE
        Polarity.NEGATIVE
        Polarity.SIZE_OF_POLARITY
        """
        is_ = p.InstrumentSettings()
        for e in [ p.Polarity.POLNULL,
                   p.Polarity.POSITIVE,
                   p.Polarity.NEGATIVE,
                   p.Polarity.SIZE_OF_POLARITY,]:

            is_.setPolarity(e)
            assert is_.getPolarity() == e

    def test_SourceFile(self):
        """
        @tests:
         SourceFile.__init__
         SourceFile.getFileSize
         .getFileType
         .getChecksum
         .getChecksumType
         .getNameOfFile
         .getPathToFile
         .getNativeIDType
         .setFileSize
         .setFileType
         .setChecksum
         .setNameOfFile
         .setPathToFile
         .setNativeIDType

        ChecksumType.SHA1
        .MD5
        .UNKNOWN_CHECKSUM
        .SIZE_OF_CHECKSUMTYPE

        MSSpectrum.__init__
        .setSourceFile
        .getSourceFile

        @end
        """
        sf = p.SourceFile()
        sf.setFileSize(123)
        sf.setFileType("test type")
        sf.setChecksum("0x123", p.ChecksumType.SHA1)
        sf.setNameOfFile("test.mzXML")
        sf.setPathToFile("./test.mzXML")
        sf.setNativeIDType("scan=")

        assert sf.getFileSize()  == 123
        assert sf.getFileType()  == "test type"
        assert sf.getChecksum()  == "0x123"
        assert sf.getChecksumType() == p.ChecksumType.SHA1
        assert sf.getNameOfFile()  == "test.mzXML"
        assert sf.getPathToFile()  == "./test.mzXML"
        assert sf.getNativeIDType()  == "scan="

        assert p.ChecksumType.SHA1 > -1
        assert p.ChecksumType.MD5 > -1
        assert p.ChecksumType.UNKNOWN_CHECKSUM > -1
        assert p.ChecksumType.SIZE_OF_CHECKSUMTYPE > -1

        spec = p.MSSpectrum()
        spec.setSourceFile(sf)
        sf = spec.getSourceFile()
        assert sf.getFileSize()  == 123
        assert sf.getFileType()  == "test type"
        assert sf.getChecksum()  == "0x123"
        assert sf.getChecksumType() == p.ChecksumType.SHA1
        assert sf.getNameOfFile()  == "test.mzXML"
        assert sf.getPathToFile()  == "./test.mzXML"
        assert sf.getNativeIDType()  == "scan="

    def test_DataValue(self):
        """
        @tests:
        DataValue.__init__
        .intValue
        .stringValue
        .floatValue
        .stringList
        @end
        """
        
        dint = p.DataValue(3)
        assert dint.intValue() == 3
        dstr = p.DataValue("uwe") 
        assert dstr.stringValue() == "uwe"
        dflt = p.DataValue(0.125)
        assert dflt.floatValue()  == 0.125
        sl = p.StringList(["a","b"])
        dslst= p.DataValue(sl)
        
        assert dslst.stringList() == sl, dslst.stringList()

        self.assert_exception(dint.stringValue, AssertionError)
        self.assert_exception(dstr.intValue, AssertionError)
        self.assert_exception(dflt.intValue, AssertionError)
        self.assert_exception(dslst.intValue, AssertionError)

        
   
    def assert_exception(self, callable_, error_type):

        ex = None
        try:
            callable_()
        except Exception as e:
            ex = e
        assert type(ex) == error_type
        


if __name__ == "__main__":
    unittest.main()
