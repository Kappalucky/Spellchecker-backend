# Spellchecker-backend

This folder contains the Django built backend for the Spellchecker application

## Getting Started

Typically I remove all secret keys and place important information within ENV files but for this application I left everything in. I strongly recommend for you to do so [remove sensitive data] if you plan on forking this repository for personal use.

#### Prerequisites

- [Python 3.0+](https://www.python.org/)
- [Pip3](https://pypi.org/project/pip/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) * Optional

#### Installation

1.  Install prerequisites
2.  Create a Python environment or Virtualenv environment
```
python3 -m venv <name or path of environment folder>
```

or

```
virtualenv venv
```
3.  Activate environment
```
source <name/path of enrivonment folder>/bin/activate
```
4.  Install requirements file from repository
```
pip3 install -r requirements.txt
```
5.  (./manage.py or Python3 manage.py) Makemigrations and migrate before running server
```
python3 manage.py makemigrations
python3 manage.py migrate
```
7.  Run the development server. Server defaults to localhost:31337. You can manually change the port if needed.
```
python3 manage.py runserver
```

Change port

```
python3 manage.py runserver 8000
```