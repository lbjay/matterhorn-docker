import os
import sys
from os.path import abspath, dirname

from fabric.api import task, local, env
from fabric.context_managers import settings, cd, hide
from fabric.contrib.console import confirm
from fabric.colors import cyan, red
from fabric.utils import abort
from fabric.decorators import with_settings

env.base_dir = abspath(dirname(__file__))
env.show_cmd = False
env.image_name = "hdce/matterhorn"
env.container_name = "hdce-matterhorn"

def docker(cmd, sudo=False, **kwargs):
    with cd(env.base_dir):
        sudo = sudo and "sudo" or ""
        cmd = "%s docker %s" % (sudo, cmd)
        if env.show_cmd:
            print cyan(cmd) 
        else:
            return local(cmd, **kwargs)

def sudo_docker(cmd, **kwargs):
    return docker(cmd, True, **kwargs)
    
env.docker = docker

@task
def name(prefix="hdce",name="matterhorn"):
    """
    set alternative prefix & name for image and container. default prefix = "hdce", name = "matterhorn". 
    """
    env.image_name = "%s/%s" % (prefix, name)
    env.container_name = "%s-%s" % (prefix, name)
    
@task
def show():
    """
    output generated commands rather than executing (i.e., dry-run)
    """
    env.show_cmd = True

@task
def sudo():
    """
    execute commands via sudo
    """
    env.docker = sudo_docker

@task
@with_settings(warn_only=True)
def build():
    """
    build the container
    """
    env.docker("build -t %s ." % env.image_name)
        
@task
@with_settings(warn_only=True)
def rmi():
    """
    remove the image
    """
    env.docker("rmi %s" % env.image_name)
        
@task
@with_settings(warn_only=True)
def run(ep='', detach=False, **kwargs):
    """
    execute the container
    
    ep - specify an alternate entrypoint, e.g., "ep=bash"
    **kwargs - additional kwargs will be converted to environment variables passed to container
    
    """ 
    ports = "-p 8080:8080"
    evars = len(kwargs) and ' '.join(["-e %s=%s" % (x[0],x[1]) for x in kwargs.items()]) or '' 
    detach = detach and "-d" or ""
    env.docker("run %s -t -i --name %s %s %s %s %s" \
               % (detach, env.container_name, evars, ports, env.image_name, ep))
    
@task
@with_settings(warn_only=True)
def stop():
    """
    stop the container
    """
    env.docker("stop %s" % env.container_name)
    
@task
@with_settings(warn_only=True)
def rm():
    """
    remove the container
    """
    env.docker("rm %s" % env.container_name)
    
@task
@with_settings(warn_only=True)
def attach():
    """
    attach to the running container
    """
    env.docker("attach %s" % env.container_name)
    
    