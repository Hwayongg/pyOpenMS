from libcpp.string cimport *
from libcpp.vector cimport *

cdef extern from "<OpenMS/DATASTRUCTURES/StringList.h>" namespace "OpenMS":
    
    cdef cppclass StringList:
        StringList()
        StringList(StringList)
        StringList(vector[string])
        int size()
        string at(int)