from fabric.api import task, sudo, env
from fabric.context_managers import cd
from fabric.contrib.console import confirm


@task
def off():
    """
    fab staging swap.off
    """
    sudo('/sbin/swappoff -a')


@task
def on():
    """
    fab staging swap.on
    """
    sudo('/sbin/swappon -a')


@task(default=True)
def free():
    """
    fab staging swap or fab staging swap.free
    """
    off()
    on()

