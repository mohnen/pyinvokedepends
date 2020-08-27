tag:
	git tag ${TAG} -m "${MSG}"
	git push --tags

venv:
	virtualenv -p python3 $@

requirements: venv requirements.txt
	. venv/bin/activate; pip install --upgrade -r requirements.txt > /dev/null

upgrade: requirements
	. venv/bin/activate; pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

dist: requirements
	. venv/bin/activate; python setup.py sdist bdist_wheel

publish-test: dist
	. venv/bin/activate; twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish: dist
	. venv/bin/activate; twine upload dist/*

test: requirements
	. venv/bin/activate; tox

coverage: test
	. venv/bin/activate; coverage report

docs: requirements
	. venv/bin/activate; cd docs; make html
	open docs/_build/html/index.html

clean:
	find . | grep '\.backup' | xargs rm

.PHONY: dist docs
