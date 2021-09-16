#!/usr/bin/python3
""" Fabirc file to compress web_static folder """

from datetime import datetime
from fabric.api import local


def do_pack():
    """do_pack - function"""

    try:
        local("mkdir -p versions")
        now = datetime.now()

        strPathNow = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            str(now.year).zfill(4),
            str(now.month).zfill(2),
            str(now.day).zfill(2),
            str(now.hour).zfill(2),
            str(now.minute).zfill(2),
            str(now.second).zfill(2)
            )
        tgzPath = "versions/web_static_{}.tgz".format(strPathNow)
        local("tar -czvf {} web_static".format(tgzPath))
        return tgzPath
    except:
        return None
