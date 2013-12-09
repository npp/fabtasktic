from fabric.api import env, sudo, task
from fabric.context_managers import cd


@task
def compile(compile_path):
    """
    fab staging compass.compile:path
    """
    with cd(compile_path):
        sudo('compass compile', user=env.www_user)
