# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _spectral_range.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_spectral_range', [dirname(__file__)])
        except ImportError:
            import _spectral_range
            return _spectral_range
        if fp is not None:
            try:
                _mod = imp.load_module('_spectral_range', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _spectral_range = swig_import_helper()
    del swig_import_helper
else:
    import _spectral_range
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


SHARED_PTR_DISOWN = _spectral_range.SHARED_PTR_DISOWN
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
class SpectralRange(full_physics_swig.generic_object.GenericObject):
    """
    We have a number of different spectrums that appear in different parts
    of the code.

    The spectrum may represent radiances, solar spectrum, solar absorption
    spectrum, etc. In addition to different units, the value may have a
    Jacobian associated with it (e.g., the results for RadiativeTransfer),
    or an uncertainty (e.g., the Level 1b data). For many purposes, it is
    convenient to treat these as essentially the same thing.

    This class captures this behavior. The data can be accessed just as
    data, as data possibly with a Jacobian, and possibly with an
    associated uncertainty. The data will always be present, but depending
    on the type of Spectrum the uncertainty or jacobian may be zero size
    arrays, indicating they aren't present.

    Similar to SpectralDomain, there doesn't seem to be a commonly used
    name for "stuff that is the Y-axis of a spectral plot". We use the
    name "SpectralRange" where "Range" is used like "Domain and
    Range" of a function. Perhaps a better name will arise and we can
    rename this class.

    Note that there are a few closely related classes, with similar
    sounding names. See spectrum_doxygen for a description of each of
    these.

    C++ includes: spectral_range.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        FullPhysics::SpectralRange::SpectralRange()
        Default constructor needed for SWIG. 
        """
        _spectral_range.SpectralRange_swiginit(self,_spectral_range.new_SpectralRange(*args))
    def _v_data(self):
        """
        blitz::Array<double, 1>& FullPhysics::SpectralRange::data()
        Underlying data. 
        """
        return _spectral_range.SpectralRange__v_data(self)

    @property
    def data(self):
        return self._v_data()

    def _v_uncertainty(self):
        """
        const blitz::Array<double, 1>& FullPhysics::SpectralRange::uncertainty() const
        Uncertainty.

        May be size 0 if we don't have an associated uncertainty. 
        """
        return _spectral_range.SpectralRange__v_uncertainty(self)

    @property
    def uncertainty(self):
        return self._v_uncertainty()

    def _v_units(self):
        """
        const Unit& FullPhysics::SpectralRange::units() const
        Units of data. 
        """
        return _spectral_range.SpectralRange__v_units(self)

    @property
    def units(self):
        return self._v_units()

    def _v_data_ad(self):
        """
        ArrayAd<double, 1>& FullPhysics::SpectralRange::data_ad()
        Underlying data, possibly with a Jacobian.

        The jacobian may have size 0. 
        """
        return _spectral_range.SpectralRange__v_data_ad(self)

    @property
    def data_ad(self):
        return self._v_data_ad()

    def convert(self, *args):
        """
        SpectralRange SpectralRange::convert(const Unit &R) const
        Convert to given units. 
        """
        return _spectral_range.SpectralRange_convert(self, *args)

    @classmethod
    def pickle_format_version(cls):
      return 1

    def __reduce__(self):
      return _new_from_init, (self.__class__, 1, self.data_ad,self.units,self.uncertainty)

    __swig_destroy__ = _spectral_range.delete_SpectralRange
SpectralRange._v_data = new_instancemethod(_spectral_range.SpectralRange__v_data,None,SpectralRange)
SpectralRange._v_uncertainty = new_instancemethod(_spectral_range.SpectralRange__v_uncertainty,None,SpectralRange)
SpectralRange._v_units = new_instancemethod(_spectral_range.SpectralRange__v_units,None,SpectralRange)
SpectralRange._v_data_ad = new_instancemethod(_spectral_range.SpectralRange__v_data_ad,None,SpectralRange)
SpectralRange.convert = new_instancemethod(_spectral_range.SpectralRange_convert,None,SpectralRange)
SpectralRange.__str__ = new_instancemethod(_spectral_range.SpectralRange___str__,None,SpectralRange)
SpectralRange_swigregister = _spectral_range.SpectralRange_swigregister
SpectralRange_swigregister(SpectralRange)



