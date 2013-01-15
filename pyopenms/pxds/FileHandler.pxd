from MSExperiment  cimport *
from libcpp.string cimport string as libcpp_string

cdef extern from "<OpenMS/FORMAT/FileHandler.h>" namespace "OpenMS":

    cdef cppclass FileHandler:  # wrap=True
        FileHandler()
        FileHandler(FileHandler)
        # cython does not support free template args, so Peak1D has
        # to be used as a fixed argument
        void loadExperiment(libcpp_string, MSExperiment[Peak1D, ChromatogramPeak] &) except+
        void storeExperiment(libcpp_string, MSExperiment[Peak1D, ChromatogramPeak]) except+
