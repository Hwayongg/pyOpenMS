#encoding: utf-8
from DelegateClassGenerator import Generator, Code
from Types import Type



    


if __name__ == "__main__":

    import sys, glob
    g = Generator()
    g.parse_all(glob.glob("pxd/*.pxd"))

    StringList    = Type(u"StringList")
    string_vector = Type("vector", False, False, False, [ Type("string") ])

    #g.add_result_alias(StringList, string_vector)
    #g.add_input_alias(StringList, string_vector)


    c = Code()
    c.addCode(g.generate_startup(), indent=0)

    c += "cimport numpy as np"
    c += "import numpy as np"

    

    for clz_name in ["Peak1D", "Precursor", "MSExperiment",
                    "InstrumentSettings", "ChromatogramTools", "Polarity",
                    "MzXMLFile", "MzMLFile", "MzDataFile", "StringList",
                    "SourceFile", "ChecksumType", "DataValue" ]:

       c.addCode(g.generate_code_for(clz_name), indent=0)

    c.addCode(g.generate_code_for("MSSpectrum"), indent=0)

    c.addFile("MSSpectrumHelpers.pyx", indent=1)

    with open("_pyOpenMS.pyx", "w") as out: 
        c.write(out=out)
