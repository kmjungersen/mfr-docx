""" Docx renderer module."""

import pydocx

def render_html(fp, *args, **kwargs):

    """Checks for OpenXML format:  OpenXML Formats have a trailer
    with "PK," followed by 18 bytes.  Rendering will proceed
    for docx, pptx, xlsx
    """
    docx_sig = "PK"
    fp.seek(-26, 2)
    tail = fp.read()

    if docx_sig not in tail:
        return 'Error: this file is not an OpenXML format.'
    else:
        return pydocx.Docx2Html(fp).parsed