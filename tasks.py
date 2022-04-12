from invoke import task, Collection
from libs.inv import run
import os


@task(default=True)
def default(ctx):
	""" List of all tasks """
	os.system("inv --list")


ns = Collection()
ns.add_collection(run)
ns.add_task(default)
