DeprecationWarning
==================

This package has been migrated to meta_exc on PyPI and will no longer be pip 
installable through ``pip install exc`` after 2019-06-17. Please update your codebase
to use ``pip install meta_exc``.

The exc package
===============

The ``exc`` package provides a metaclass for exceptions, allowing
on-the-spot subclassing, e.g. in order to have one exception class per
raise site. It is easy to use, as the following example illustrates ::

    import exc

    class FruitError(exc.Exception):
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

There are wrapped versions of all the builtins: ``exc.TypeError``,
``exc.IOError`` and so forth. The metaclass is called
``DerivableException``.

The intended usage of ``exc`` is for each exception site to raise an
exception with a unique class, so that they may be caught
individually.


Shorthand syntax
================

``exc.Exception['a/b'] == exc.Exception.specialize('a/b') == exc.Exception.specialize('a').specialize('b')``

Compatibility
=============

``exc`` should work with Python >= 2.6 and Python >= 3. It does not
work in Python 2.4 because of limitations on exception types. In
Python 3, try/except does not consult instancehook or subclasshook, so
``exc.Exception`` cannot be used to catch plain ``Exception`` (but it
can be in Python 2).


