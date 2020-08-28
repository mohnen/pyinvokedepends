from invoke import task
from pyinvokedepends import depends

@depends(on=["./hello.c"], creates=["./a.out"])
@task
def test(c):
  #c.run("gcc hello.c")
  c.run("touch a.out", echo=True)
