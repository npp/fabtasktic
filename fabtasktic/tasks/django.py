from fabric.api import env, sudo, task
from fabric.context_managers import cd


@task
def collectstatic():
    """
    fab staging django.collectstatic
    """
    with settings(warn_only=True):
        with cd(env.project_path):
            sudo('%s && %s' % (env.activate, 'python manage.py collectstatic --noinput'), user=env.www_user)
