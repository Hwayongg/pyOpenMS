from libcpp cimport *
from Types cimport *
from DPosition cimport *

cdef extern from "<OpenMS/KERNEL/Peak1D.h>" namespace "OpenMS":

    cdef cppclass Peak1D:
        Peak1D()               nogil except +
        Peak1D(Peak1D &)               nogil except +
        Real getIntensity()     nogil except +
        DoubleReal getMZ()     nogil except +
        void setMZ(DoubleReal)  nogil except +
        void setIntensity(Real) nogil except +
        bool operator==(Peak1D) nogil except +
        bool operator!=(Peak1D) nogil except +
