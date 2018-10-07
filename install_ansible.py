#!/usr/bin/python

import subprocess, platform

def check_os():
    """Check if your os is a macos"""

    if platform.system() != "Darwin":
        print "This script only works on macos system"
        exit(1)

def install_pip(pkg_version=None):
    """Install pip in local user"""
    # FIXME: https://github.com/ansible/ansible-container/issues/919

    if pkg_version:
        pkg_name = "pip==" + pkg_version
    else:
        pkg_name = "pip"

    try:
        subprocess.check_call(["easy_install", "--user", pkg_name])
    except subprocess.CalledProcessError:
        print "[Error] while installing pip"

def install_ansible():
    """Install ansible"""

    try:
        subprocess.check_call(["pip", "install", "--user", "ansible"])
    except subprocess.CalledProcessError:
        print "[Error] while installing ansible"

def upgrade_setuptools():
    """Upgrade setuptools"""
    # FIXME: https://github.com/facebook/prophet/issues/418

    try:
        subprocess.check_call(["pip", "install", "--upgrade", "--user", "setuptools"])
    except subprocess.CalledProcessError:
        print "[Error] while upgrading setuptools"

def downgrade_docker(pkg_version=None):
    """Downgrade docker"""
    # FIXME: https://github.com/ansible/ansible-container/issues/884

    if pkg_version:
        pkg_name = "docker==" + pkg_version
    else:
        pkg_name = "docker"

    try:
        subprocess.check_call(["pip", "install", "--upgrade", "--user", pkg_name])
    except subprocess.CalledProcessError:
        print "[Error] while downgrading docker"

def install_ansible_container():
    """Install ansible-container"""

    try:
        subprocess.check_call(["pip", "install", "--user", "ansible-container[docker]"])
    except subprocess.CalledProcessError:
        print "[Error] while installing ansible-container"

if __name__ == "__main__":
    check_os()
    install_pip("9.0.3")
    install_ansible()
    upgrade_setuptools()
    downgrade_docker("2.7.0")
    install_ansible_container()
