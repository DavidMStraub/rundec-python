%module rundec

%{
#include <stdlib.h>
#include <utility>

#include "CRunDec3/CRunDec.3.1.h"
%}

%include "std_pair.i"
%include "std_vector.i"
%include carrays.i

namespace std {
    %template(PairDouble)          pair<double,double>;
    %template(PairDoubleVector)    vector<pair<double,double> >;
}

%array_class(TriplenfMmu, TriplenfMmuArray)
%array_class(RunDecPair, RunDecPairArray)
%include "CRunDec3/CRunDec.3.1.h"
