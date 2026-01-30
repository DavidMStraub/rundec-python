%module rundec

%begin %{
#define Py_LIMITED_API 0x030A0000
%}

%{
#include <stdlib.h>
#include <utility>

#include "CRunDec3/CRunDec.h"

// Define RunDecPair as typedef for compatibility
typedef std::pair<double,double> RunDecPair;
%}

%include "std_string.i"
%include "std_pair.i"
%include "std_vector.i"
%include carrays.i

namespace std {
    %template(PairDoubleVector)    vector<pair<double,double> >;
}

// Create RunDecPair from std::pair<double,double>
%template(RunDecPair) std::pair<double,double>;

%array_class(TriplenfMmu, TriplenfMmuArray)

// Make the array accept std::pair<double,double> (which is what RunDecPair creates)
// by telling SWIG that std::pair<double,double> can be used as RunDecPair
%typemap(in) RunDecPair {
  void *argp = 0;
  int res = SWIG_ConvertPtr($input, &argp, SWIGTYPE_p_std__pairT_double_double_t, 0 | 0);
  if (!SWIG_IsOK(res)) {
    SWIG_exception_fail(SWIG_ArgError(res), "in method '" "$symname" "', argument " "$argnum"" of type '" "$1_type""'");
  }
  if (!argp) {
    SWIG_exception_fail(SWIG_NullReferenceError, "invalid null reference " "in method '" "$symname" "', argument " "$argnum"" of type '" "$1_type""'");
  }
  $1 = *reinterpret_cast<std::pair<double,double> *>(argp);
}

// Handle RunDecPair* (pointer) arguments - accept either RunDecPairArray or a single RunDecPair
%typemap(in) std::pair<double,double>* (std::pair<double,double> temp) {
  void *argp = 0;
  // Try RunDecPairArray first
  int res = SWIG_ConvertPtr($input, &argp, SWIGTYPE_p_RunDecPairArray, 0 | 0);
  if (SWIG_IsOK(res)) {
    // It's a RunDecPairArray, use it directly
    $1 = reinterpret_cast<std::pair<double,double> *>(argp);
  } else {
    // Try single std::pair<double,double> (RunDecPair)
    res = SWIG_ConvertPtr($input, &argp, SWIGTYPE_p_std__pairT_double_double_t, 0 | 0);
    if (SWIG_IsOK(res)) {
      // It's a single RunDecPair, store in temp and pass its address
      temp = *reinterpret_cast<std::pair<double,double> *>(argp);
      $1 = &temp;
    } else {
      SWIG_exception_fail(SWIG_ArgError(res), "in method '" "$symname" "', argument " "$argnum"" of type '" "$1_type""'");
    }
  }
}

// Typecheck typemap for overload resolution - accept either RunDecPairArray or single RunDecPair
%typemap(typecheck,precedence=SWIG_TYPECHECK_POINTER) std::pair<double,double>* {
  void *vptr = 0;
  // Check if it's a RunDecPairArray
  int res = SWIG_ConvertPtr($input, &vptr, SWIGTYPE_p_RunDecPairArray, 0);
  if (SWIG_IsOK(res)) {
    $1 = 1;
  } else {
    // Check if it's a single RunDecPair (std::pair<double,double>)
    res = SWIG_ConvertPtr($input, &vptr, SWIGTYPE_p_std__pairT_double_double_t, 0);
    $1 = SWIG_IsOK(res) ? 1 : 0;
  }
}

%array_class(RunDecPair, RunDecPairArray)

%include "CRunDec3/CRunDec.h"
