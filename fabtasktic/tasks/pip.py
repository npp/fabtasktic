from fabric.api import env, sudo, task


@task
def freeze(packagename=None):
    """
    fab staging pip.freeze
    """
    sudo('%(bin_path)s/pip freeze' % env, env.env_user)


@task
def install(packagename=None):
    """
    fab staging pip.install:packagename[==X.X.X]
    """
    if packagename is not None:
        env.packagename = packagename
        sudo('%(bin_path)s/pip install %(packagename)s' % env, env.env_user)
    else:
        raise ValueError("Missing package name")


@task
def uninstall(packagename=None):
    """
    fab staging pip.uninstall:packagename
    """
    if packagename is not None:
        env.packagename = packagename
        sudo('%(bin_path)s/pip uninstall %(packagename)s' % env, env.env_user)
    else:
        raise ValueError("Missing package name")


@task
def upgrade(packagename=None):
    """
    fab staging pip.upgrade:packagename[==X.X.X]
    """
    if packagename is not None:
        env.packagename = packagename
        sudo('%(bin_path)s/pip install -U %(packagename)s' % env, env.env_user)
    else:
        raise ValueError("Missing package name")
