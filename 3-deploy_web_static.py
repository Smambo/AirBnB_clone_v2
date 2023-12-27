#!/usr/bin/python3
"""Import modules for Fabric script."""
import os.path
from fabric.api import env
from fabric.api import local
from fabric.api import run
from fabric.api import put
from datetime import datetime

env.hosts = ["54.172.41.19", "54.152.233.230"]


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


def do_deploy(archive_path):
    """Distributes archive to web servers
    Args:
        archive_path: path of the archive
    Returns:
        False if file doesn't exist at archive_path
        Otherwise True.
    """
    if os.path.isfile(archive_path) is False:
        return (False)
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return (False)
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return (False)
    if run("mkdir -p /data/web_static/releases/{}/".
            format(name)).failed is True:
        return (False)
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(file, name)).failed is True:
        return (False)
    if run("rm /tmp/{}".format(file)).failed is True:
        return (False)
    if run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".
            format(name, name)).failed is True:
        return (False)
    if run("rm -rf /data/web_static/releases/{}/web_static".
            format(name)).failed is True:
        return (False)
    if run("rm -rf /data/web_static/current").failed is True:
        return (False)
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name)).failed is True:
        return (False)
    return (True)


def deploy():
    """
    Generates and distributes archive to web servers.
    """
    file = do_pack()

    if file is None:
        return (False)
    return (do_deploy(file))
