
# flask-backend-template

Basic template to quickly create new flask applications.

## Quick setup

* Install *venv* module from pip if you don't have it installed already and create new venv folder (.venv in this case):

        $ py -3 -m pip install venv
        $ py -3 -m venv .venv

* Before installing or running the server always activate the env:

        $ .venv\scripts\activate[.bat]
        $ deactivate[.bat]

* After that install default required packages (edit *req.txt* or *add_req.txt* before if you want to change something) and install one or both as you wish:

        $ python -m pip install -r requirements.txt
        $ python -m pip install -r additional_requirements.txt

## Running

### Windows
    
* Simply execute *run.bat* (will execute *./run.ps1* which will load environment variables from *app/.env* and start server in specified mode:

        $ run.bat [debug|prod]

### Linux
* Source *app/.env* file and start server using gunicorn or similar server (not included yet)
