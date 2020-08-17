#!/usr/bin/env bash
from fabric.api import *
from datatime import datatime


def do_pack():
    """ script that generates a .tgz archive from the contents of the web_static
    folder of your AirBnB Clone repo, using the function do_pack."""
    local("sudo mkdir -p versions")
    times = datetime.now().strftime("%Y%m%d%H%M%S")
    files = ("versions/web_static_{}.tgz").format(times)
    local("sudo tar -cvzf {} web_static".format(files))
    return files
