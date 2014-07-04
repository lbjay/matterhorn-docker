matterhorn-docker
=================

vagrant/docker setup for running a [matterhorn](http://opencast.org/matterhorn/) instance

## requirements

#### if using vagrant

* a working [vagrant](http://www.vagrantup.com/)

That's it!

#### pure docker

* [docker](http://docker.io) (tested with v1.0)
* python [fabric](http://fabfile.org) (optional if you want to use the provided fabric commands)

## vagrant setup

This part is optional; you can instead just skip right to [building/running](#building/running) if you have a working docker instance on your current machine.

1. clone this repo
1. `vagrant up`
1. `vagrant ssh`
1. Now that you're inside the vagrant vm, `cd /vagrant`

## building, running & stopping

1. `fab build` to build the `hdce/matterhorn` image
1. `fab run` to run the `hdce-matterhorn` container. 
1. `Ctrl+C` when finished
1. `fab rm` to remove the container before running again

*Note*: the fabric commands can be chained together, for instance `fab rm build run`.

## run detached

By default the container will execute and start up the matterhorn service in the foreground. To run in detached mode use `fab run:detach=1`. You can then use `fab attach` to attach to the running container afterwards.

## alternate cmd

By default docker will start the container by running the matterhorn `start_matterhorn.sh` script. To start with a different *entrypoint*, for instance a bash shell, use `fab:ep=bash`. 

This is useful for debugging and development as it lets you get inside the running container to inspect and do things. You can then run `start_matterhorn.sh` manually once inside.

