%module rundec

%{
#include <stdlib.h>
#include <utility>

#include "CRunDec3/CRunDec.3.1.h"
%}

%include "std_pair.i"

namespace std {
    %template(PairDouble)   pair<double,double>;
}

%include "CRunDec3/CRunDec.3.1.h"
