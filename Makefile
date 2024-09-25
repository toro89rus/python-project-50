install:
	poetry install

test:
	poetry run pytest

cov:
	poetry run pytest --cov=gendiff --cov-report term-missing

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-install-venv:
	python3 -m pip install dist/*.whl

package-install-pipx:
	pipx install dist/*.whl

lint:
	poetry run flake8 gendiff

cognitive:
	poetry run complexipy gendiff
	poetry run flake8 --max-cognitive-complexity=5 gendiff

package-uninstall:
	python3 -m pip uninstall --user hexlet-code

package-uninstall-venv:
	python3 -m pip uninstall hexlet-code

package-uninstall-pipx:
	pipx uninstall hexlet-code

package-update-venv:
	make build
	python3 -m pip install --force-reinstall dist/*.whl
