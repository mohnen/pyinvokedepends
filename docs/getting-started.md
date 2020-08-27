# Getting Started

PyPi template is hosted on PyPi, so...

```bash
$ pip install pypi-template
```

## Use PyPi Template to setup a new package

```bash
$ mkdir my-new-project
$ cd my-new-project
$ git init
$ pypi-template

```

PyPi template will ask you to provide some basic information, which allows it to generate several files for your. All files that are written are reported. When ready, you have a fresh, customized source tree.

## Minimal things to edit

1. module top-level folder

There is a placeholder `pypi_template` top-level module folder. You'll probably want to rename that to your own package/module name and populate it with your own code ;-)

```bash
$ mv pypi_template your_new_project
```

2. docs/

The `docs/` a copy of PyPi Templates own docs. These can be published to [ReadTheDocs](https://readthedocs.org) (see below). You can edit those files to accommodate your project.

> **NOTE regarding editing generated files:** you can re-run `pypi-template`, and it will regenerate files that have changed. This is useful if you have made changes to `.pypi-template`, which contains your provided values. In case of the actual documentation, which contains no variables, you can add these files to the `skip` variable in the `.pypi-template` file, to avoid them being overwritten.

> **I said "minimal"!** Of course you can also change the default MIT License (probably a great [issue](https://github.com/christophevg/pypi-template/issues) to register, to allow choosing one ;-) )

## Things to do

Besides providing you with a lot of boilerplate (configuration) files, there are also things to do...

### Testing

A basic testing setup has been prepared. To run it locally, issue...

```bash
$ make test
...
___________________________________ summary ____________________________________
  py27: commands succeeded
  congratulations :)
```

Head over to [https://travis-ci.org](https://travis-ci.org) and register your project. A basic CI configuration is also provided.

Head over to [https://coveralls.io](https://coveralls.io) and register your project to consult your code coverage reporting.

### Generate/Publish Documentation

```bash
$ make docs
```

This wil generate a HTML version of your `docs/` and open it in a browser.

If you want to publish your documentation (from the [docs/](docs/) folder) to e.g. [ReadTheDocs](https://readthedocs.org), import the repository over there also.

### Publishing to PyPi

Head over to [https://test.pypi.org](https://test.pypi.org) and register for an account. Next simply issue...

```bash
$ make publish-test
```

to publish your module to the test instance of PyPi.

or

```bash
$ make publish
```

to publish your module to the main instance of [PyPi](https://pypi.org).
