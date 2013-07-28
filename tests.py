# -*- coding: utf-8 -*-
import random

from base36 import to64, from64, to36, from36
import pytest


def test_to64():
    assert to64(0) == '0'
    assert to64(10) == 'a'
    assert to64(125) == '1Z'
    assert to64(126) == '1='
    assert to64(127) == '1_'
    assert to64(128) == '20'
    assert len(to64(pow(3, 1979))) == 523
    with pytest.raises(AssertionError):
        to64(-1)
    with pytest.raises(AssertionError):
        to64('a')


def test_from64():
    assert from64('0') == 0
    assert from64('a') == 10
    assert from64('1Z') == 125
    assert from64('1=') == 126
    assert from64('1_') == 127
    assert from64('20') == 128
    with pytest.raises(ValueError):
        from64('!')


def test_custom_alphabet64():
    CUSTOM = 'abcdefghijklmnopqrstuvwxyz0123456789.:,;*@#$%&/()[]{}=_-ABCDEFGH'

    assert to64(555, CUSTOM) == 'i$'
    assert from64('AA', CUSTOM) == 3640

    RANDOM = [
        c for c in
        '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ=_'
    ]
    random.shuffle(RANDOM)
    RANDOM = ''.join(RANDOM)

    RCUSTOM = [c for c in CUSTOM]
    random.shuffle(RCUSTOM)
    RCUSTOM = ''.join(RCUSTOM)

    rnum = random.randint(0, 5555)

    assert from64(to64(rnum, CUSTOM), CUSTOM) == rnum
    assert from64(to64(rnum, RANDOM), RANDOM) == rnum
    assert from64(to64(rnum, RCUSTOM), RCUSTOM) == rnum


def test_custom_alphabet64_invalid():
    CUSTOM = 'abcdefghijklmnopqrstuvwxyz0123456789.:,;*@#$%&/()[]{}=_-ABCDEFGH'

    # bad custom alphabet
    with pytest.raises(AssertionError):
        to64(1, 'bad')
    with pytest.raises(AssertionError):
        to64(1, CUSTOM + '!-')

    # values not in custom alphabet
    with pytest.raises(ValueError):
        from64('J', CUSTOM)
    with pytest.raises(ValueError):
        from64('!', CUSTOM)


def test_to36():
    assert to36(0) == '0'
    assert to36(10) == 'a'
    assert to36(125) == '3h'
    assert to36(143) == '3z'
    assert to36(144) == '40'
    assert len(to36(pow(3, 1979))) == 607
    with pytest.raises(AssertionError):
        to36(-1)
    with pytest.raises(AssertionError):
        to36('a')


def test_from36():
    assert from36('0') == 0
    assert from36('a') == 10
    assert from36('3h') == 125
    assert from36('3z') == 143
    assert from36('40') == 144
    with pytest.raises(ValueError):
        from36('!')


def test_custom_alphabet36():
    CUSTOM = '9876543210ZYXWVUTSRQPONMLKJIHGFEDCBA'

    assert to36(555, CUSTOM) == 'UU'
    assert from36('ZZ', CUSTOM) == 370

    RANDOM = [c for c in '0123456789abcdefghijklmnopqrstuvwxyz']
    random.shuffle(RANDOM)
    RANDOM = ''.join(RANDOM)

    RCUSTOM = [c for c in CUSTOM]
    random.shuffle(RCUSTOM)
    RCUSTOM = ''.join(RCUSTOM)

    rnum = random.randint(0, 5555)

    assert from36(to36(rnum, CUSTOM), CUSTOM) == rnum
    assert from36(to36(rnum, RANDOM), RANDOM) == rnum
    assert from36(to36(rnum, RCUSTOM), RCUSTOM) == rnum


def test_custom_alphabet36_invalid():
    CUSTOM = '9876543210ZYXWVUTSRQPONMLKJIHGFEDCBA'

    # bad custom alphabet
    with pytest.raises(AssertionError):
        to36(1, 'bad')
    with pytest.raises(AssertionError):
        to36(1, CUSTOM + 'abc')

    # values not in custom alphabet
    with pytest.raises(ValueError):
        from36('ab', CUSTOM)
    with pytest.raises(ValueError):
        from36('!', CUSTOM)
