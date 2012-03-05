# -*- coding: utf-8 -*-
"""
    Draft
    -----
    Prototyping Web Development

    :copyright: (c) 2012 By Ori Livneh
    :license: GPLv3, see LICENSE for more details.
"""
import os

from draft import Draft
from flask import render_template

app = Draft(__name__)
app.mount('/cwd/', os.getcwd())

@app.route('/')
@app.route('/<script>/')
def draft(script=None):
    if not script.endswith('.js'):
        script += '.js'
    return render_template('draft.html', script=script)
