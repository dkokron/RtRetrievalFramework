# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (3,0,0):
    new_instancemethod = lambda func, inst, cls: _cost_func.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cost_func', [dirname(__file__)])
        except ImportError:
            import _cost_func
            return _cost_func
        if fp is not None:
            try:
                _mod = imp.load_module('_cost_func', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _cost_func = swig_import_helper()
    del swig_import_helper
else:
    import _cost_func
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


SHARED_PTR_DISOWN = _cost_func.SHARED_PTR_DISOWN
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

import full_physics_swig.problem_state
import full_physics_swig.generic_object
class CostFunc(full_physics_swig.problem_state.ProblemState):
    """
    The base class for all problem classes that implement a cost function.

    The class CostFunc is the base class for all problem classes that
    implement a cost function (a scalar real function with a range that
    never includes negative numbers).

    A cost function only (without derivatives of any order) can be
    optimized by methods such as the Sampling Method that do not require
    derivatives of any order.

    C++ includes: cost_func.h 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _cost_func.delete_CostFunc
    def cost(self):
        """
        virtual double FullPhysics::CostFunc::cost()=0
        The cost function.

        This method must be implemented by the classes derived from this
        class.

        The parameters (the point in the parameter space) must have already
        been set before calling this method. The parameters are already set if
        parameters() method (see ProblemState class) or cost_x() method are
        already called successfully. If the parameters are already set, then
        this method returns the value of the cost function at the current set
        point.

        Cost function value 
        """
        return _cost_func.CostFunc_cost(self)

    def cost_x(self, *args):
        """
        virtual double FullPhysics::CostFunc::cost_x(const blitz::Array< double, 1 > &x)
        The cost function with parameters.

        This method also evaluates the cost function; however, it sets the
        problem at the input new point and then evaluates the cost function.

        Parameters:
        -----------

        x:  New set of parameters

        Cost function value 
        """
        return _cost_func.CostFunc_cost_x(self, *args)

    def _v_num_cost_evaluations(self):
        """
        virtual int FullPhysics::CostFunc::num_cost_evaluations() const
        Returns the number of the times cost has been evaluated.

        The number of the times cost has been evaluated. 
        """
        return _cost_func.CostFunc__v_num_cost_evaluations(self)

    @property
    def num_cost_evaluations(self):
        return self._v_num_cost_evaluations()

    def zero_num_evaluations(self):
        """
        virtual void FullPhysics::CostFunc::zero_num_evaluations()
        Sets cost evaluation counter to zero. 
        """
        return _cost_func.CostFunc_zero_num_evaluations(self)

CostFunc.cost = new_instancemethod(_cost_func.CostFunc_cost,None,CostFunc)
CostFunc.cost_x = new_instancemethod(_cost_func.CostFunc_cost_x,None,CostFunc)
CostFunc._v_num_cost_evaluations = new_instancemethod(_cost_func.CostFunc__v_num_cost_evaluations,None,CostFunc)
CostFunc.zero_num_evaluations = new_instancemethod(_cost_func.CostFunc_zero_num_evaluations,None,CostFunc)
CostFunc_swigregister = _cost_func.CostFunc_swigregister
CostFunc_swigregister(CostFunc)



