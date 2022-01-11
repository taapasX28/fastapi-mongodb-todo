# FastAPI MongoDB Todo App

## Install Dependencies

1. fastAPI
2. uvicorn
3. pymongo

```shell
$ pip install fastapi uvicorn pymongo pymongo[srv]
```

## To Launch:

Use  `uvicorn main:app` to launch the app backend.

## Directory tree:

```shell
├── config
│   └── database.py
├── models
│   └── todos_model.py
├── routes
│   └── todos_route.py
├── schemas
│   └── todos_schema.py
├── README.md
└──main.py
```

* Config contains the database configration for linking to mongodb database. Modify <password> and <id> to link your db.
* `model` contains the the database structure.
* `routes` defines the ways to interact with the db using fastapi. Comments are added to explain the functionalty of each route
* To test the app use ` http://127.0.0.1:8000/docs` to use requests with pyapi