### Hexlet tests and linter status:
[![Actions Status](https://github.com/Treskun4eg/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Treskun4eg/python-project-52/actions)
[![task_manager](https://github.com/Treskun4eg/python-project-52/actions/workflows/task_manager_check.yml/badge.svg)](https://github.com/Treskun4eg/python-project-52/actions/workflows/task_manager_check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/1c0d87dcf24887258c89/maintainability)](https://codeclimate.com/github/Treskun4eg/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1c0d87dcf24887258c89/test_coverage)](https://codeclimate.com/github/Treskun4eg/python-project-52/test_coverage)

### PREVIEW
https://task-manager-hia7.onrender.com

### Task Manager

This is an application that allows you to set tasks, indicate tags and statuses.
![Авторизация](https://cdn2.hexlet.io/derivations/image/original/eyJpZCI6IjQ0YWQ5NmU4ODg4M2FmNjQzY2Q0NDk2ODdkY2IxNjA5LnBuZyIsInN0b3JhZ2UiOiJjYWNoZSJ9?signature=99f42fbf385e3edff99b0f369f561793478d8be02b0593707898d70ed406742a)
![Привет](https://cdn2.hexlet.io/derivations/image/original/eyJpZCI6IjZjZGE5NDgxMDBiYTdhYjYyNDY0NWVhMWI2MGI4ZWVhLnBuZyIsInN0b3JhZ2UiOiJjYWNoZSJ9?signature=b0a97936e97fa31dfd06a5013a90effe20be352dd142ce9ddf53748842c221cc)
![Задачи](https://cdn2.hexlet.io/derivations/image/original/eyJpZCI6IjA1MGY1MTc5ZjJkMTJhZjk2N2E3OWMyYzhhYjg0N2Q5LnBuZyIsInN0b3JhZ2UiOiJjYWNoZSJ9?signature=39fa5674a2ef9c60338539540b36423cedf327f28b57c43c62ce7416513c10f4)

### To work with the application you will need to set secret keys

#### Secret keys
Create a file for environment variables with the following data in the task_manager .env directory:  
DATABASE_URL=postgresql://{username}:{password}@{host}:{port}/{databasename}  
SECRET_KEY='{your secret key}'

### Run project

#### Install dependencies
```make install```  
#### Preparing the Database
```make migrate```  
#### Launch of the project
```make start```

#### Deployment commands
```make install```
```make start```
