from fabric.api import env, sudo, task
from fabric.context_managers import cd


@task
def compile(task=None):
    """
    fab staging grunt.compile:task
    """
    compile_path=env.project_path
    with cd(compile_path):
        if task is not None:
            sudo('grunt %s' % task, user=env.www_user)
        else:
            sudo('grunt', user=env.www_user)
