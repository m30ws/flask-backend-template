
# flask-backend-template

Basic template to quickly create new flask applications.

## Quick setup

* Install *venv* module from pip if you don't have it installed already and create new venv folder (**.venv** in this case):

        $ py -3 -m pip install venv
        $ py -3 -m venv .venv

* Before installing or running the server always activate the environment:

        $ .venv\scripts\activate[.bat]
        $ deactivate[.bat]

* After that install default required packages (edit `requirements.txt` or `additional_requirements.txt` before if you want to change something) and install one or both as you wish:

        $ python -m pip install -r requirements.txt
        $ python -m pip install -r additional_requirements.txt
        
* if you want to enable HTTPS
    * place `privatekey.key` and `certificate_chain.pem`/`certificate.crt` into **ssl**/ folder
    * uncomment the respective lines in `app/server.py`:

          server.ssl_module            = 'builtin'
          server.ssl_private_key       = '../ssl/privatekey.key'
          server.ssl_certificate       = '../ssl/certificate.crt'
          server.ssl_certificate_chain = '../ssl/certificate_chain.pem'

## Running

### Windows
        
* Simply execute `run.bat` (will execute `./run.ps1` which will load environment variables from `app/.env` and start server in specified mode:

        $ run.bat [debug|prod]

### Linux
* Source `app/.env` file and start server using gunicorn or similar server (not included yet)
