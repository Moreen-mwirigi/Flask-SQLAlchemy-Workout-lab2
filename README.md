# Workout API
A RESTful API for tracking workouts and exercises built with Flask, SQLAlchemy, and Marshmallow.

## Features
1. Create, read and delete workouts
2. Create, read and delete Exercises
3. Link Exercises to Workouts with reps, sets and duration via WorkoutExercise join table
4. Data validation with Marshmallow and SQLAlchemy vlidates.
5. SQLite database with Flask-Migrate

## Tech Stack
- Flask
- SQLite + SQLAlchemy ORM
- Flask-Marshmallow + marshmallow-sqlalchemy
- Flask-Migrate
- Pipenv

## Installation
1. **Install dependencies**
    `pipenv install` `pipenv shell`
2. **Setup Database**
    Create tables `pipenv run flask db upgrade`
3. **Seed Database**
    `pipenv run ython seed.py`
4. **Run Server**
    `pipenv run python app.py`

## API Endpoints
    Method              Endpoint                Description
    GET                     /                   Welcome message
    GET                   /workouts             Get all workouts
    GET                /workouts/<id>           Get single workout
    POST                /workouts               Create workout
    DELETE             /workouts/<id>           Delete wokout
    GET                 /exercises              Get all exercises
    GET                /exercises/<id>          Get single exercise
    POST                /exercises              Create exercise
    DELETE             /exercises/<id>          Delete exercise
    POST            /workout/<workout_id>/exercise/<exercise_id>/workout_exercise   Link exercise to workout

## Create a Workout
curl -X POST http://127.0.0.1:5000/workouts\
-H "Content-Type: application/json"\
-d '{"date": "2024-01-15", "duration": 60}'

## Create an Exercise
curl -X POST http://127.0.0.1:5000/exercises\
-H "Content-Type: application/json"\
-d '{"name": "Push Up", "category": "Strength", "weight": 0}'

## Link Exercise to Workout
curl -X POST http://127.0.0.1:5000/workout/1/exercises/1/workout_exercise\
-H "Content-Type: application/json"\
-d '{"reps": 10, "sets": 3, "duration_seconds": 60}'

## Get all Exercises
curl http://127.0.0.1:5000/exercises\

## Project Structure
.
|- config.py  
|- models.py  #Workout, Exercise, WorkoutExercise models
|- schemas.py # Marshmallow schemas for validation
|- app.py # Routes/Controllers
|- seed.py # Seed data for testing
|- migrations/
|- instance
        |- app.db #SQLite databases
|- Pipfile
|- README.md
