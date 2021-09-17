#!/usr/bin/python3
""" Fabirc file to compress web_static folder """

from datetime import datetime
from fabric.api import local, env
from fabric.operations import run, put
from pathlib import Path

env.hosts = ["ubuntu@3.95.61.247", "ubuntu@104.196.45.214"]


def do_pack():
    """ create current tgz version from folder web_static """

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
        local("tar -czvf {} web_static".format(strPathNow))
        return strPathNow
    except:
        return None


def do_deploy(archive_path):
    """ Distributes among servers do_pack file """

    if Path(archive_path).is_file():
        try:
            put(archive_path, '/tmp/')
            path = (str(archive_path).split('.'))[0].split('/')
            run("mkdir -p /data/web_static/releases/{}/".format(path[1]))
            run("tar -xzf {} -C {}".format(
                "/tmp/{}.tgz".format(path[1]),
                "/data/web_static/releases/{}".format(path[1])
            ))

            run("rm /tmp/{}.tgz".format(path[1]))
            run("mv {} {}".format(
                "/data/web_static/releases/{}/web_static/*".format(path[1]),
                "/data/web_static/releases/{}/".format(path[1])
            ))
            run("rm -rf {}".format(
                "/data/web_static/releases/{}/web_static".format(path[1])
            ))
            run("rm -rf /data/web_static/current")
            run("ln -s {} {}".format(
                "/data/web_static/releases/{}/".format(path[1]),
                "/data/web_static/current"
            ))
            return True
        except:
            return False
    else:
        return False


def deploy():
    """ full deployment with previous functions """
    path = do_pack()
    if path is not None:
        return do_deploy(path)
    else:
        return False
