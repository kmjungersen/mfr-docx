# -*- coding: utf-8 -*-
import mock

import mfr
import pytest

from mfr_docx import Handler as DocxHandler

@pytest.fixture
def fakefile():
    """A simple file-like object"""
    return mock.Mock(spec=file)

def setup_function(func):
    mfr.register_filehandler(DocxHandler)
    mfr.config['STATIC_URL'] = '/static

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


def test_render(fakefile):
    assert False, 'finish me'