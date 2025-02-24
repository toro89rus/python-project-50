install:
	uv sync

test:
	uv run pytest
lint:
	uv run ruff check gendiff
cov:
	uv run pytest --cov=gendiff --cov-report xml

print-cov:
	uv run pytest --cov=gendiff --cov-report term-missing

gendiff:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-uninstall:
	uv tool uninstall hexlet-code
