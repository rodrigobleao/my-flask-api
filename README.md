## Original

https://github.com/codeshow/003-arquitetura-flask.git

## Create new database

```bash
flask create-db
flask populate-db
flask add-user -u admin -p 1234
flask run
```

## Structure

```bash
.
├── Makefile
├── API  (MAIN PACKAGE)
│   ├── app.py  (APP FACTORIES)
│   ├── blueprints  (BLUEPRINT FACTORIES)
│   │   ├── __init__.py
│   │   ├── restapi  (REST API)
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   │   └── webui  (FRONT END)
│   │       ├── __init__.py
│   │       ├── templates
│   │       │   ├── index.html
│   │       │   └── product.html
│   │       └── views.py
│   ├── ext (EXTENSION FACTORIES)
│   │   ├── admin.py
│   │   ├── appearance.py
│   │   ├── auth.py
│   │   ├── commands.py
│   │   ├── configuration.py
│   │   ├── database.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── models.py  (DATABASE MODELS)
│   └── tests  (TESTS)
│       ├── conftest.py
│       ├── __init__.py
│       └── test_api.py
├── README.md
├── requirements_dev.txt
├── requirements_test.txt
├── requirements.txt
└── settings.toml  (SETTINGS)

```
