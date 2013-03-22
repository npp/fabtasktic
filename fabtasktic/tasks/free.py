from fabric.api import task, run


@task(default=True)
def free():
    """
    fab staging free.free                   Checks available free memory/swap
    """
    run('free -t -m')