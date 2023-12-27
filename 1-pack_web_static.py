#!/usr/bin/python3
"""Import modules for Fabric script."""
import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from contents of web_static folder.
    """
    dutc = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            dutc.year,
            dutc.month,
            dutc.day,
            dutc.hour,
            dutc.minute,
            dutc.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return (None)
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return (None)
    else:
        return (file)
