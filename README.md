Use this to scaffhold Flask apps with some convenience libraries. I wrote it using Python 3.7 on Mac. It might break with other Python versions and operating systems.

To use, you will need to:

- Create a virtual environment on you local machine in your project directory and activate it
- Download the zip of this repository and copy the contents into your project directory
- Run `pip install -r requirements.txt`
- In the root of your project
  - Create a `.gitignore` file in the with the following content:
    ```
    .env
    .vscode

    venv/

    *.pyc
    __pycache__/

    instance/

    .pytest_cache/
    .coverage
    htmlcov/

    dist/
    build/
    *.egg-info/
    ```
  - Create a `.env` file and define the following variables
    - `JWT_SECRET_KEY`: You need to keep this super duper secret and you'll want to change it on a regular basis if your app is in production and handling user passwords or any other remotely sensitive data. You can generate it with something like:
      ```
      import os
      import binascii
      binascii.hexlify(os.urandom(24))
      ```
    - `DATABASE_URL`: For a postgres backend, it should look like: `postgres://{user}:{password}@{hostname}:{port}/{database_name}`
    - (**optional**) Define `FLASK_APP` and `FLASK_ENV` variables here. With `python-dotenv` installed, this should allow you
    to use the flask cli without having to define these variables in the terminal. Mine look like:
      ```
      FLASK_APP=wsgi.py
      FLASK_ENV=development
      ```
- Once the `FLASK_APP` and `DATABASE_URL` environment variables are set, you can (and should) create your database by running:
  ```
  $ flask db init

  $ flask db migrate

  $ flask db upgrade

  $ flask seed-db

  ```
- Now the `/api/auth/register` and `/api/auth/login` endpoints should work and you'll have to take it from here...