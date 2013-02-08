from libcpp cimport bool
from libcpp.vector cimport vector as libcpp_vector
from DataValue cimport *
from String cimport *
from Types cimport *
from MetaInfoInterface cimport *
from ProteinHit cimport *

cdef extern from "<OpenMS/METADATA/ProteinIdentification.h>" namespace "OpenMS":

    cdef cppclass ProteinIdentification(MetaInfoInterface):
        # wrap-inherits:
        #    MetaInfoInterface

        ProteinIdentification() nogil except +
        bool operator==(ProteinIdentification) nogil except +

        libcpp_vector[ProteinHit] getHits() nogil except +
        void insertHit(ProteinHit) nogil except +
        void setHits(libcpp_vector[ProteinHit]) nogil except +

        # cython has a problem with inheritance of overloaded methods,
        # so we do not declare them here, but separately in each derived
        # class which we want to be wrapped:
        void getKeys(libcpp_vector[String] & keys)
        void getKeys(libcpp_vector[unsigned int] & keys)
        DataValue getMetaValue(unsigned int) nogil except +
        DataValue getMetaValue(String) nogil except +
        bool metaValueExists(String) nogil except +
        bool metaValueExists(unsigned int) nogil except +
        void removeMetaValue(String) nogil except +
        void removeMetaValue(unsigned int) nogil except +
