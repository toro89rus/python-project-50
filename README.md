### Hexlet tests and linter status:
[![Actions Status](https://github.com/toro89rus/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/toro89rus/python-project-50/actions)


### CodeClimate
[![Maintainability](https://api.codeclimate.com/v1/badges/d1f7bd9b4db58d3c846a/maintainability)](https://codeclimate.com/github/toro89rus/python-project-50/maintainability)


### CodeClimate Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/d1f7bd9b4db58d3c846a/test_coverage)](https://codeclimate.com/github/toro89rus/python-project-50/test_coverage)

# Gendiff
Command-line app that compare two JSON/YAML files and presents difference in your console

## Requirements
- Python 3.12
- Poetry
- make
- pip
- pipx(optional)

## How to install
```
git clone git@github.com:toro89rus/python-project-50.git
make build
make package-install
```

Due to limitations of using pip to install (including install --user) packages on Debian 12+ or Ubuntu 23+ (see [details](https://packaging.python.org/en/latest/specifications/externally-managed-environments/#externally-managed-environments)) there are two ways of installing Brain Games if you are are using one of these operation systems:
- using virtual enviroment. Make sure venv is [installed in your system](https://virtualenv.pypa.io/en/latest/installation.html). Don't forget to activate your venv before installation.

```
git clone git@github.com:toro89rus/python-project-50.git
make build
make package-install-venv
```

- if you don't know how to use venv, you can install Brain Games via pipx, which will automatically create a virtual environment for you and install Brain Games there. Make sure pipx is [installed in your system](https://pipx.pypa.io/stable/installation/)

```
git clone git@github.com:toro89rus/python-project-50.git
make build
make package-install-pipx
```

## How to uninstall
Use one of these commands according to the one you used for installation:

```
make package-uninstall
```

```
make package-uninstall-venv
```

```
make package-uninstall-pipx
```

### Comparing files, default format(stylish)
[![asciicast](https://asciinema.org/a/C4Ysfs1J4drQf0iHdh2lqvc6s.svg)](https://asciinema.org/a/C4Ysfs1J4drQf0iHdh2lqvc6s)

### Comparing files, plain format
[![asciicast](https://asciinema.org/a/fDgmjY1bVOO5IK63thE9dNXFW.svg)](https://asciinema.org/a/fDgmjY1bVOO5IK63thE9dNXFW)

### Comparing files, json format
[![asciicast](https://asciinema.org/a/JLPHUNxfrM9OCae5DTIT2xSxh.svg)](https://asciinema.org/a/JLPHUNxfrM9OCae5DTIT2xSxh)
