from . import __delegate_int__
import types


def extension(supertype):
    """
    Decorator to get Swift-like extensions in Python (ew)
    """
    name = str()
    try:
        name = supertype.__name__

    except NameError:
        raise TypeError('{} is not known:'.format(supertype))

    def extension_wrap1(thing):
        # ensure that we are aware of the super class to extend
        if name not in __delegate_int__:
            __delegate_int__[name] = dict()

        # case 1: we used @extension() on a function
        if isinstance(thing, types.FunctionType):

            if thing.__name__ not in __delegate_int__[name]:
                __delegate_int__[name][thing.__name__] = thing

            def extension_wrap2(*args, **kwargs):
                return thing(*args, **kwargs)

            return extension_wrap2

        # case 2: we used @extension on a class
        elif isinstance(thing, types.ClassType):

            thing_impl = thing()
            # allow extending state... we need access to supertype's delegates.
            # looks like we get to grief python again... keep a separate list
            # of 'init hooks' which run whenever a supertype object is
            # instantiated, to do this work of adding the correct state.
            # this is a w f u l
            # oh no... how do we extend based on class..?
            delegates_cls = super(delegates, thing_impl)
            if delegates_cls.del_attrs is None:
                delegates_cls.del_attrs = dict()

            # delegates_cls.del_attrs[thing.__name__] = thing()
            # oh shit, what do I do here... do we include new state?
            # how do we do it?
            functions_in_class = filter(lambda x: isinstance(x,
                                        types.FunctionType),
                                        (getattr(thing, x) for x in dir(thing)))
            for func in functions_in_class:
                __delegate_int__[name][func.__name__] = func

            return thing

        # case 3: we used @extension() on something else. disregard.
        else:
            return thing

    return extension_wrap1


class delegates(object):
    """
    delegate class to inherit in order to have access to the delegate system.
    DO NOT OVERRIDE __getattr__
    """
    # allow extending state
    __slots__ = ('del_attrs',)

    def __getattr__(self, attr):
        """
        how does this work
        """
        if type(self).__name__ in __delegate_int__:
            if attr in __delegate_int__[type(self).__name__]:
                return __delegate_int__[type(self).__name__][attr]

            else:
                raise AttributeError(attr)

        else:
            raise AttributeError(attr)
