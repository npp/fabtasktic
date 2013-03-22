from fabric.api import task, sudo, env
from fabric.context_managers import cd
from fabric.contrib.console import confirm


@task
def off():
    """
    fab staging swap.off
    """
    sudo('swappoff -a')


@task
def on():
    """
    fab staging swap.on
    """
    sudo('swappon -a')


@task(default=True)
def reset():
    """
    fab staging swap or fab staging swap.reset
    """
    off()
    on()

