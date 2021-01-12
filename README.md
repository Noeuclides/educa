# E-Learning Platform

This is a e-learning platform with its own CMS (Content Management System).

## Requirements
In order to run the application correctly you have to have python 3.7.6 version or greater and
[pyenv](https://pipenv-es.readthedocs.io/es/latest/) environment tool installed.

## Installation

Clone the repository and go to the educa project where the manage.py file is and install from Pipfile.

```bash
git clone https://github.com/Noeuclides/educa.git
cd educa/educa
pipenv install
```

Then you can activate the Pipenv shell:
```bash
pipenv shell
python --version
```

Now you can run the django application.
```bash
python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 10, 2021 - 21:44:29
Django version 3.0.10, using settings 'educa.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```