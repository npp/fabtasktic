from fabric.api import env, sudo, task, settings
from fabric.context_managers import cd


@task
def collectstatic():
    """
    fab staging django.collectstatic
    """
    with settings(warn_only=True):
        with cd(env.project_path):
            sudo('%s && python manage.py collectstatic --noinput --settings=%s' % (env.activate, env.django_settings), user=env.www_user)
