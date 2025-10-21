#!/usr/bin/env python
import pytest

"""Tests for `xdb_location` package."""

# from xdb_location import xdb_location


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyfeldroy/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string



def test_vector_index_search():
    from xdb_location.xdb_location import searchWithContent
    ttt = searchWithContent(target_ip="1.15.241.228")
    assert ttt == "中国|0|北京|北京市|方正宽带"
