#!/usr/bin/python3
"""Import modules for Fabric script."""
import os
from fabric.api import *

env.hosts = ["54.172.41.19", "54.152.233.230"]


def do_clean(number=0):
    """Script deletes out-of-date archives.
    Args:
        number (int); number of archives to keep.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
