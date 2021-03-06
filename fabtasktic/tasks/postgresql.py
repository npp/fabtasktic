from . import (start_service, stop_service, status_service,
               reload_service, force_reload_service, restart_service)
from fabric.api import task

SERVICE = 'postgresql'


@task
def start():
    """
    fab staging postgresql.start
    """
    start_service(SERVICE)


@task
def stop():
    """
    fab staging postgresql.stop
    """
    stop_service(SERVICE)


@task
def status():
    """
    fab staging postgresql.status
    """
    status_service(SERVICE)


@task
def reload():
    """
    fab staging postgresql.reload
    """
    reload_service(SERVICE)


@task
def force_reload():
    """
    fab staging postgresql.force_reload
    """
    force_reload_service(SERVICE)


@task
def restart():
    """
    fab staging postgresql.restart          Will display status when restart complete
    """
    restart_service(SERVICE)
    status()
