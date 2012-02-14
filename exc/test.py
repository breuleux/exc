
import exc as E

ExcA = E.IOError["A"]

class _Special(OSError):
    def __init__(self, x):
        self.x = x

# This works in both 2.x and 3.x
Special = E.DerivableException('Special', (_Special,), {})

class Derived(E.OSError):
    def __init__(self, y):
        self.y = y

def errA0():
    raise ExcA('test')

def errA1():
    raise E.IOError.specialize("A")

def errS0(x):
    raise Special(x)

def errS1(x):
    raise Special['abc/def'](x)



def test_sanity_check():
    try:
        errA0()
    except IOError:
        pass

def test_sanity_check_2():
    v = 1234
    try:
        errS0(v)
    except OSError as err:
        assert err.x == v

def test_simple():
    try:
        errA0()
    except ExcA:
        pass

def test_cache1():
    try:
        errA1()
    except ExcA:
        pass

def test_cache2():
    try:
        errA0()
    except E.IOError["A"]:
        pass

def test_special():
    v = 900
    try:
        errS1(v)
    except Special as s:
        assert s.x == v

def test_special_2():
    v = 900
    try:
        errS1(v)
    except Special['abc']['def'] as s:
        assert s.x == v

def test_special_3():
    try:
        try:
            errS1(None)
        except Special['abc']['wrong'] as s:
            # This should not catch the error
            raise TypeError('wrong')
    except Exception as e:
        assert not isinstance(e, TypeError)

def test_derived():
    v = 666
    try:
        raise Derived['and_so!'](v)
    except Derived as e:
        assert e.y == v


def test_hooks():
    assert isinstance(IOError("test"), E.IOError)
    assert issubclass(IOError, E.IOError)

def test_subclasshook():
    print("test_subclasshook: This test is known to fail in Python 3.x"
          + " because the except statement does not seem to consult"
          + " __instance/subclasshook__.")
    try:
        raise IOError("this should not get through")
    except E.IOError as e:
        pass

