#Einfacher Test in pytest
#@author Jan Strothmann

import pytest
from exampleclass import ExampleClass 

def test_tautology():
    assert True

def test_constructor_basic():
    testobject=ExampleClass(2)
    assert testobject != None

def test_constructor_advanced():
    testobject=ExampleClass(2)
    assert type(testobject) == ExampleClass

def test_compute():
    testobject=ExampleClass(2)
    assert testobject.compute(2)== 4

def test_Exception():
    testobject=ExampleClass(2)
    assert testobject.compute("g")!= 4