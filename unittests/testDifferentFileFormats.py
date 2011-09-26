import unittest, sys, win32api
import pyOpenMS

def show_mem(label):
    t = win32api.GlobalMemoryStatus()
    v, p = t['AvailVirtual'], t['AvailPhys']
    v /= 1024.0 * 1024
    p /= 1024.0 * 1024

    print (label+" ").ljust(30, "."), ": %8.2f MB" % p
    sys.stdout.flush()


class TestLoadAndStoreInDifferentFileFormats(unittest.TestCase):

    def test000(self):

        print
        print
        show_mem("start")
        
        p = pyOpenMS.PyMzXMLFile()
        e = pyOpenMS.PyMSExperiment()

        p.load("test.mzXML", e)
        self.check(e)
        show_mem("after load mzXML")

        ct = pyOpenMS.PyChromatogramTools()
        ct.convertChromatogramsToSpectra(e)
        p.store("test.mzXML", e)
        show_mem("after store mzXML")

        p.load("test.mzXML", e)
        self.check(e)
        show_mem("after load mzXML")

        p = pyOpenMS.PyMzMLFile()
        ct.convertSpectraToChromatograms(e, True)
        p.store("test.mzML", e)
        show_mem("after store mzML")
        p.load("test.mzML", e)
        self.check(e)
        show_mem("after load mzML")

        p = pyOpenMS.PyMzDataFile()
        ct.convertChromatogramsToSpectra(e)
        p.store("test.mzData", e)
        show_mem("after store mzData")
        p.load("test.mzData", e)
        self.check(e)
        show_mem("after load mzData")

        del e
        del p
        del ct
        show_mem("after cleanup")

    def check(self, e):
        assert e.size() == 2884

        spec = e[0]
        assert (spec.getRT()-0.00291) < 0.0001
        assert spec.getMSLevel() == 1 
        assert spec.size() == 281
        assert spec.getName() == ""


if __name__ == "__main__":
    unittest.main()