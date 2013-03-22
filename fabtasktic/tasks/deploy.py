from fabric.api import task, sudo, env
from fabric.context_managers import cd
from fabric.contrib.console import confirm


@task(default=True)
def deploy(branch="master"):
    """
    fab staging deploy OR fab staging deploy:branchname
    """
    if confirm("Are you sure you want to deploy to %s" % env.host):
        pre()
        with cd(env.repo_path):
            sudo('git checkout %s' % branch, user=env.www_user),
            sudo('git pull', user=env.www_user)
            sudo('git submodule update', user=env.www_user)
            sudo('touch %(conf_path)s/*.wsgi' % env)
        post()


def pre():
    pass


def post():
    pass
