#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""
from fabric import api
import time


def do_pack():
    """Generate an tgz archive from web_static folder"""
    try:
        api.local("mkdir -p versions")
        api.local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except:
        return None
