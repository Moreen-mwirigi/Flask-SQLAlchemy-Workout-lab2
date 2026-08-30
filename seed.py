from config import db, create_app
from models import Workout, Exercise, WorkoutExercise
from datetime import date

app = create_app()

with app.app_context():
    print("Clearing existing data...")
    WorkoutExercise.query.delete()
    Exercise.query.delete()
    Workout.query.delete()

    print("Seeding Exercises...")
    exercise1 = Exercise(name="Push-Up", category="Strength", weight=0)
    exercise2 = Exercise(name="Squat", category="Strength", weight=0)
    exercise3 = Exercise(name="Running", category="Cardio", weight=0)
    db.session.add_all([exercise1, exercise2, exercise3])
    db.session.commit()

    print("Seeding Workouts...")
    workout1 = Workout(name="Morning Routine", date=date.today(), duration=30, notes="A quick morning workout.")
    workout2 = Workout(name="Evening Routine", date=date.today(), duration=45, notes="A longer evening workout.")
    db.session.add_all([workout1, workout2])
    db.session.commit()

    print("Seeding join...")
    we1 = WorkoutExercise(workout_id=workout1.id, exercise_id=exercise1.id, sets=3, reps=15, duration_seconds=300)
    we2 = WorkoutExercise(workout_id=workout1.id, exercise_id=exercise2.id, sets=3, reps=20, duration_seconds=500)
    we3 = WorkoutExercise(workout_id=workout2.id, exercise_id=exercise3.id, sets=1, reps=1, duration_seconds=1800)
    db.session.add_all([we1, we2, we3])
    db.session.commit()
    print("Seeding completed.")
