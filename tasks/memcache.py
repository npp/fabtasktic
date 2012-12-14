from fabtasktic.tasks import (start_service, stop_service, status_service,
                             reload_service, force_reload_service, restart_service)
from fabric.api import task

SERVICE = 'memcached'

@task
def start():
    '''
    fab staging memcache.start
    '''
    start_service(SERVICE)

@task
def stop():
    '''
    fab staging memcache.stop
    '''
    stop_service(SERVICE)

@task
def status():
    '''
    fab staging memcache.status
    '''
    status_service(SERVICE)

@task
def force_reload():
    '''
    fab staging memcache.force_reload
    '''
    force_reload_service(SERVICE)

@task
def restart():
    '''
    fab staging memcache.restart          Will display status when restart complete
    '''
    restart_service(SERVICE)
    status()
