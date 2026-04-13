import pytest
from selenium import webdriver
from praktikum.burger import Burger


@pytest.fixture
def burger():
    burger = Burger()
    return burger
