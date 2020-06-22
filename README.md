# FastAPI-Calculator
The simple calculator based on FastAPI framework.

## What you need for running the App
Git, Python 3, Pipenv, Docker

## How to get and run the App

* Clone the App repository
`git clone https://github.com/msydor3nko/FastAPI-Calculator.git`

* Enter to the 'FastAPI-Calculator' directory
`cd FastAPI-Calculator`

* Activate virtual environment
`pipenv shell`

* Install all needed libraries from Pipfile
`pipenv install --dev`

* Run MongoDB into Docker container using 'docker-compose.yml' file
`docker-compose up`

* Run ASGI server with App
`uvicorn main:app --reload`

* Enter by provided link in '/docs' to interact with the App

* Also, you can testing the App using PyTest as in the comand bellow
`pytest -v`
