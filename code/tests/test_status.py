from MCPoly import status
from MCPoly import view3d
import pytest
import os
import re

@pytest.fixture
def current1():
    return status('Atoms1',loc='./data_status/')

def test1_status_status1(current1):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current1.status(figureonly=True)
    os.chdir(opath)
    assert len(num)==8

def test2_status_status1(current1):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current1.status(figureonly=True)
    os.chdir(opath)
    for E in num:
        assert E<=-1150.90
        
@pytest.fixture
def current1():
    return status('Atoms1',loc='./data_status/')

def test_status_statusonly1(current1):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current1.status(figureonly=True,statusonly=True)
    os.chdir(opath)
    assert num==2
    
@pytest.fixture
def current2():
    return status('Atoms2',loc='./data_status/')

def test_status_statusonly2(current2):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current2.status(figureonly=True,statusonly=True)
    os.chdir(opath)
    assert num==1

@pytest.fixture
def current3():
    return status('Atoms3',loc='./data_status/')

def test_status_statusonly3(current3):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current3.status(figureonly=True,statusonly=True)
    os.chdir(opath)
    assert num==0

@pytest.fixture
def current4():
    return status('Atoms4',loc='./data_status/')

def test_status_status4(current4):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current4.status(figureonly=True)
    os.chdir(opath)
    assert len(num)==78

@pytest.fixture
def current4():
    return status('Atoms4',loc='./data_status/')

def test_status_statusonly4(current4):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    num=current4.status(figureonly=True,statusonly=True)
    os.chdir(opath)
    assert num==4

@pytest.fixture
def current1():
    return status('Atoms1',loc='./data_status/')

def status_figure(current1):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    current1.figure(7)
    os.chdir(opath)
    return 0

@pytest.fixture
def current1():
    return status('Atoms1',loc='./data_status/')

def status_figureonly(current1):
    opath=os.getcwd()
    os.chdir('./MCPoly/tests')
    current1.figuretraj()
    os.chdir(opath)
    return 0