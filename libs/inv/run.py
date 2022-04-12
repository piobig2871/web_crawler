from invoke import task
import os


@task(default=True)
def list_process(ctx):
    """Checking if invoke tasks are working fine."""
    os.system("ps -al")
