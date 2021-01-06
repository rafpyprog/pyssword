clean:
	rm -rf build dist *.egg-info

build:
	python3 setup.py sdist bdist_wheel

publish-test:
	twine upload --repository testpypi dist/*