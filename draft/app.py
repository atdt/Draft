# -*- coding: utf-8 -*-
"""
    Draft
    -----
    Prototyping Web Development

    :copyright: (c) 2012 By Ori Livneh
    :license: GPLv3, see LICENSE for more details.
"""
import os

from flask import Flask, render_template
from werkzeug import SharedDataMiddleware


class Draft(Flask):
    def mount(self, dir, mountpoint):
        self.wsgi_app = SharedDataMiddleware(self.wsgi_app, {dir: mountpoint})

app = Draft(__name__)
app.mount('/cwd/', os.getcwd())

@app.route('/')
@app.route('/<script>/')
def draft(script=None):
    if not script.endswith('.js'):
        script += '.js'
    return render_template('draft.html', script=script)
