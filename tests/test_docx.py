# -*- coding: utf-8 -*-
import mock

import mfr
import pytest


from mfr_docx import Handler as DocxHandler
from mfr_docx.render import render_html


@pytest.fixture
def fakefile():
    """A simple file-like object"""
    return mock.Mock(spec=file)

def setup_function(func):
    mfr.register_filehandler(DocxHandler)
    mfr.config['STATIC_URL'] = '/static'

def teardown_function(func):
    mfr.core.reset_config()


@pytest.mark.parametrize('filename', [
    'file.docx',
])
def test_detect_docx_extension(fakefile, filename):
    fakefile.name = filename
    handler = DocxHandler()

    assert handler.detect(fakefile) is True

@pytest.mark.parametrize('filename', [
    'file.doc',
    'file.txt',
])
def test_dont_detect_docx_extension(fakefile, filename):
    fakefile.name = filename
    handler = DocxHandler()
    assert handler.detect(fakefile) is False


### Content rendering tests ###
fp = open('sample.docx', 'r')
content = render_html(fp)

def test_render_text():
    assert 'Lorem ipsum' in content

def test_for_unicode():
    assert isinstance(content, unicode)

def test_for_html_tags():
    assert '<div' in content

def test_for_bold():
    assert '<strong>' in content

def test_for_unicode_character():
    assert u'\xfc' in content