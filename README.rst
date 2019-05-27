DeprecationWarning
==================

This package was available under ``exc`` on PyPI and has undergone a recent
migration to ``meta_exc``. It will no longer be available to be installed via
``pip install exc`` after 2019-06-17. Please update your codebase to use 
``pip install meta_exc``.

The meta_exc package
====================

The ``meta_exc`` package provides a metaclass for exceptions, allowing
on-the-spot subclassing, e.g. in order to have one exception class per
raise site. It is easy to use, as the following example illustrates ::

    import meta_exc

    class FruitError(meta_exc.Exception):
        pass

    import sys
    fruit = sys.argv[1]

    try:
        if fruit in ('lemon', 'lime', 'grapefruit'):
            raise FruitError['too_sour']('%ss are too sour!' % fruit)
        elif fruit == 'jalapeno':
            raise FruitError['too_spicy']('%ss are too spicy!' % fruit)
        print("Nom nom")
    except FruitError['too_sour']:
        print('I did not eat the fruit because it was too sour...')
    except FruitError:
        print('I did not eat the fruit for some reason.')

There are wrapped versions of all the builtins: ``meta_exc.TypeError``,
``meta_exc.IOError`` and so forth. The metaclass is called
``DerivableException``.

The intended usage of ``meta_exc`` is for each exception site to raise an
exception with a unique class, so that they may be caught
individually.


Shorthand syntax
================

``meta_exc.Exception['a/b'] == meta_exc.Exception.specialize('a/b') == meta_exc.Exception.specialize('a').specialize('b')``

Compatibility
=============

``meta_exc`` should work with Python >= 2.6 and Python >= 3. It does not
work in Python 2.4 because of limitations on exception types. In
Python 3, try/except does not consult instancehook or subclasshook, so
``meta_exc.Exception`` cannot be used to catch plain ``Exception`` (but it
can be in Python 2).


