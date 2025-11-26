#pruebas unitarias de la funcion "sumar"
import pytest 
from operaciones import *

def test_sumar1():
    res=sumar([1,2,3] )
    assert res==6

def test_sumar2():
    res=sumar([10, 15, 20] )
    assert res==45

def test_sumar3():
    res=sumar([ ] )
    assert res==0

