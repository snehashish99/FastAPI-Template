<h1 align=center><strong>FastAPI Backend Template</strong></h1>

<br>

This is a template repository aimed to kick-start your project with a setup from a real-world application! This template utilizes the following tech stack:

* 🐍 [FastAPI](https://fastapi.tiangolo.com/)
* 🐘 [Async PostgreSQL with SQLAlchemy](https://pypi.org/project/databases/)
* 🐳 [Dockerized](https://www.docker.com/)


## Why the above Tech-Stack?

Well, the easy answer is **Asynchronousity** and **Speed**!

* **FastAPI** is crowned as the fastest web framework for Python and thus we use it for our backend development.
* The database of my choice is the **asynchronous** version of **PostgreSQL** (via [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)).

## Other Technologies

The above-listed technologies are just the main ones. There are other technologies utilized in this project template to ensure that your application is robust and provides the best possible development environment for your team! These technologies are:

* [Databases with asyncpg](https://pypi.org/project/databases/)
* [Python Decouple](https://docs.pytest.org/en/7.2.x/)

## Setup Guide

This backend application is setup with `Docker`.

1. Clone the repo and go to project root
   ```shell
   cd FastAPI-Template
   ```

2. Create .env file with help of .env.example

3. Spin up containers
    ```shell
    sudo docker-compose up -d --build
    ```
4. Backend Application (API docs) -> `http://localhost:8000/docs`

Enjoy your development and may your technology be forever useful to everyone 😉🚀🧬

---