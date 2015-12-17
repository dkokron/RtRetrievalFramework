# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _fp_time.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_fp_time', [dirname(__file__)])
        except ImportError:
            import _fp_time
            return _fp_time
        if fp is not None:
            try:
                _mod = imp.load_module('_fp_time', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _fp_time = swig_import_helper()
    del swig_import_helper
else:
    import _fp_time
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


SHARED_PTR_DISOWN = _fp_time.SHARED_PTR_DISOWN
def _new_from_init(cls, version, *args):
    '''For use with pickle, covers common case where we just store the
    arguments needed to create an object. See for example HdfFile'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__(*args)
    return inst

def _new_from_set(cls, version, *args):
    '''For use with pickle, covers common case where we use a set function 
    to assign the value'''
    if(cls.pickle_format_version() != version):
      raise RuntimeException("Class is expecting a pickled object with version number %d, but we found %d" % (cls.pickle_format_version(), version))
    inst = cls.__new__(cls)
    inst.__init__()
    inst.set(*args)
    return inst

import full_physics_swig.generic_object
import datetime
import time

def _new_time(pgs):
  return Time.time_pgs(pgs)

class Time(full_physics_swig.generic_object.GenericObject):
    """
    This is a simple time class.

    There are a few reasonable choices for expressing time information. We
    could use TAI, GPS, the PGS toolkit. Each of these time system can be
    related to the other by a constant, since the only difference is the
    Epoch that time is measure against.

    For simplicity, we just use the standard unix time in seconds from
    January 1, 1970.

    This class abstracts out the representation we use for time. We supply
    conversions to the specific time systems for use in the cases that a
    specific system is needed (e.g., calling a PGS toolkit routine).

    We also supply methods for converting to and from a string
    representation of the time. We support the standard CCSDS format
    (e.g., "1996-07-03T04:13:57.987654Z").

    C++ includes: fp_time.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def time_pgs(*args):
        """
        static Time FullPhysics::Time::time_pgs(double pgs)
        Return time from given PGS toolkit time (epoch of 1993-01-01). 
        """
        return _fp_time.Time_time_pgs(*args)

    time_pgs = staticmethod(time_pgs)
    def time_unix(*args):
        """
        static Time FullPhysics::Time::time_unix(double unix_time)
        Return time from given Unix time (epoch of 1970-01-01). 
        """
        return _fp_time.Time_time_unix(*args)

    time_unix = staticmethod(time_unix)
    def _v_unix_time(self):
        """
        double FullPhysics::Time::unix_time() const
        Give time in unix time, as a double (epoch 1970-01-01) 
        """
        return _fp_time.Time__v_unix_time(self)

    @property
    def unix_time(self):
        return self._v_unix_time()

    def _v_pgs_time(self):
        """
        double FullPhysics::Time::pgs_time() const
        Give time in PGS toolkit time, as a double (epoch 1993-01-01) 
        """
        return _fp_time.Time__v_pgs_time(self)

    @property
    def pgs_time(self):
        return self._v_pgs_time()

    def parse_time(*args):
        """
        Time Time::parse_time(const std::string &Time_string)
        Parse CCSDS format time (e.g., "1996-07-03T04:13:57.987654Z") 
        """
        return _fp_time.Time_parse_time(*args)

    parse_time = staticmethod(parse_time)
    def __reduce__(self):
      return _new_time, (self.pgs(),)

      
    def __init__(self): 
        """
        Time::Time(const boost::posix_time::ptime &t)
        Create from a boost posix time. 
        """
        _fp_time.Time_swiginit(self,_fp_time.new_Time())
    __swig_destroy__ = _fp_time.delete_Time
Time._v_unix_time = new_instancemethod(_fp_time.Time__v_unix_time,None,Time)
Time._v_pgs_time = new_instancemethod(_fp_time.Time__v_pgs_time,None,Time)
Time.__str__ = new_instancemethod(_fp_time.Time___str__,None,Time)
Time.__cmp__ = new_instancemethod(_fp_time.Time___cmp__,None,Time)
Time.__add__ = new_instancemethod(_fp_time.Time___add__,None,Time)
Time.__radd__ = new_instancemethod(_fp_time.Time___radd__,None,Time)
Time.__sub__ = new_instancemethod(_fp_time.Time___sub__,None,Time)
Time_swigregister = _fp_time.Time_swigregister
Time_swigregister(Time)

def Time_time_pgs(*args):
  """
    static Time FullPhysics::Time::time_pgs(double pgs)
    Return time from given PGS toolkit time (epoch of 1993-01-01). 
    """
  return _fp_time.Time_time_pgs(*args)

def Time_time_unix(*args):
  """
    static Time FullPhysics::Time::time_unix(double unix_time)
    Return time from given Unix time (epoch of 1970-01-01). 
    """
  return _fp_time.Time_time_unix(*args)

def Time_parse_time(*args):
  """
    Time Time::parse_time(const std::string &Time_string)
    Parse CCSDS format time (e.g., "1996-07-03T04:13:57.987654Z") 
    """
  return _fp_time.Time_parse_time(*args)



