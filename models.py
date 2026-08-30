from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from config import db
from datetime import date

class Workout(db.Model, SerializerMixin):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today)
    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes
    notes = db.Column(db.Text)

    workout_exercises = db.relationship('WorkoutExercise', back_populates='workout', cascade='all, delete-orphan')

    serialize_rules = ('-workout_exercises.workout',)


class Exercise(db.Model, SerializerMixin):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., Cardio, Strength, Flexibility
    weight = db.Column(db.Float)  # Weight in kilograms
    
    workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise', cascade='all, delete-orphan')

    serialize_rules = ('-workout_exercises.exercise',)

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Exercise name cannot be empty.")
        return name

class WorkoutExercise(db.Model, SerializerMixin):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    duration_seconds = db.Column(db.Integer, nullable=False)  # Duration in seconds for cardio exercises

    workout = db.relationship('Workout', back_populates='workout_exercises')
    exercise = db.relationship('Exercise', back_populates='workout_exercises')

    serialize_rules = ('-workout.workout_exercises', '-exercise.workout_exercises')

    @validates('sets', 'reps', 'duration_seconds')
    def validate_positive_integer(self, key, value):
        if value <= 0:
            raise ValueError(f"{key.capitalize()} must be a positive integer.")
        return value