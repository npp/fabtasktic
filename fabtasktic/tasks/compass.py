from fabric.api import env, sudo, task
from fabric.context_managers import cd


@task
def compile():
    """
    fab staging compass.compile:path
    """
    compile_path=env.static_path
    with cd(compile_path):
        sudo('compass compile', user=env.www_user)
