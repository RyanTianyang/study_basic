#!/usr/bin/env python
# encoding: utf-8
import pytest
import time
import random

# def test_firstFunc():
#     assert 22==23
#     print("2")


def add(x, y):
    return x+y


def test_ass():
    pytest.assume(2==4)
    assert 3==6
    print("3")