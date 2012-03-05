# -*- coding: utf-8 -*-
"""
    Draft
    -----
    Prototyping Web Development

    :copyright: (c) 2012 By Ori Livneh
    :license: GPLv3, see LICENSE for more details.
"""
from flask import Flask
from werkzeug import SharedDataMiddleware

class Draft(Flask):
    def mount(self, dir, mountpoint):
        self.wsgi_app = SharedDataMiddleware(self.wsgi_app, {dir: mountpoint})
