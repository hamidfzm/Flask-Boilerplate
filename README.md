# Flask-Boilerplate
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

After years of web development with flask I decided to share my experience in flask applications structure.
Since I couldn't find any good boilerplate that could satisfy my needs when I start new projects.

I happily appreciate your suggestions and pull requests in order to improve this boilerplate.

## Configure
In order to setup virtual environment and dependency manager for this project run configure for first time.

```console
foo@bar:Flask-Boilerplate$ ./configure.sh
```

_Notice_ configure is using [**pipenv**](https://github.com/pypa/pipenv)

## Basic Concepts
Nothing for now

## Usage
After running configure script you can use following commands:

- Activate virtual environment
```console
foo@bar:Flask-Boilerplate$ pipenv shell
```

- Set flask app
```console
foo@bar:Flask-Boilerplate$ export FLASK_APP=application
```

- Run flask app
```console
foo@bar:Flask-Boilerplate$ flask run
```

- View flask app routes
```console
foo@bar:Flask-Boilerplate$ flask routes
```