from fabric.api import env, sudo, task
from fabric.context_managers import cd
from fabric.contrib.console import confirm


@task
def migrate(app=None, database=None):
    """
    fab staging db.migrate:appname,database
    """
    if app is None:
        raise ValueError('Missing app to migrate')
    if database is None:
        raise ValueError('Missing database flag')
    if confirm("Are you sure you want migrate %s on %s" % (app, env.host)):
        with cd(env.project_path):
            sudo('%s && python manage.py migrate %s --settings=%s --database=%s' % (env.activate, app, env.django_settings, database))
