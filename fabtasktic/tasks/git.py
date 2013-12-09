from fabric.api import env, sudo, task
from fabric.context_managers import cd


@task
def checkout(branch="master"):
    """
    fab staging git.checkout:branch
    """
    with cd(env.repo_path):
        sudo('git checkout %s' % branch, user=env.www_user)
        sudo('git pull', user=env.www_user)
