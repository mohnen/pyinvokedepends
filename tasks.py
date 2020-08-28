import os
import glob
from invoke import task

@task
def dist(c):
    for file in glob.glob('./dist/*'):
        print(f"removing {file}")
        os.remove(file)
    c.run("python setup.py sdist bdist_wheel")

@task(pre=[dist])
def publishTest(c):
	c.run("twine upload --repository-url https://test.pypi.org/legacy/ dist/*")

@task(pre=[dist])
def publish(c):
	c.run("twine upload dist/*")
