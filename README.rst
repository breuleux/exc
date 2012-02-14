
======
README
======

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

