clean:
	rm -rf build dist *.egg-info

build:
	python3 setup.py sdist bdist_wheel

publish-test:
	twine check --strict dist/*
	twine upload --repository testpypi dist/*

publish:
	twine check --strict dist/*
	twine upload dist/*
