from config import create_app, db
from models import Workout, Exercise, WorkoutExercise
from schemas import workout_schema, workouts_schema, exercise_schema, exercises_schema, workout_exercise_schema, workout_exercises_schema
from flask import request, make_response, jsonify
from marshmallow import ValidationError

app = create_app()

@app.route('/')
def home():
    return "Welcome to the Workout API!"

# Workout 
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return make_response(workouts_schema.dump(workouts), 200)

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return make_response(jsonify({"error": "Workout not found"}), 404)
    return make_response(workout_schema.dump(workout), 200)

@app.route('/workouts', methods=['POST'])
def post_workout():
    try:
        data = workout_schema.load(request.get_json())
        new_workout = workout_schema.load(data)
        db.session.add(new_workout)
        db.session.commit()
        return make_response(workout_schema.dump(new_workout), 201)
    except ValidationError as err:
        return make_response(jsonify(err.messages), 400)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return make_response(jsonify({"error": "Workout not found"}), 404)
    db.session.delete(workout)
    db.session.commit()
    return make_response(jsonify({"message": "Workout deleted"}), 204)

# Exercise
@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return make_response(exercises_schema.dump(exercises), 200)

@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return make_response(jsonify({"error": "Exercise not found"}), 404)
    return make_response(exercise_schema.dump(exercise), 200)

@app.route('/exercises', methods=['POST'])
def post_exercise():
    try:
        data = exercise_schema.load(request.get_json())
        new_exercise = Exercise(**data)
        db.session.add(new_exercise)
        db.session.commit()
        return make_response(exercise_schema.dump(new_exercise), 201)
    except ValidationError as err:
        return make_response(jsonify(err.messages), 400)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)

@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return make_response(jsonify({"error": "Exercise not found"}), 404)
    db.session.delete(exercise)
    db.session.commit()
    return make_response(jsonify({"message": "Exercise deleted"}), 204)

# JOIN
@app.route('/workout/<int:workout_id>/exercises/<int:exercise_id>/workout_exercise', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    Workout = Workout.query.get(workout_id)
    exercise = Exercise.query.get(exercise_id)
    if not Workout:
        return make_response(jsonify({"error": "Workout not found"}), 404)
    if not exercise:
        return make_response(jsonify({"error": "Exercise not found"}), 404)
    try:
        data = request.get_json()
        full = {"workout_id": workout_id, "exercise_id": exercise_id, **data}
        validated = workout_exercise_schema.load(full)
        new_workout_exercise = WorkoutExercise(workout_id=workout_id, exercise_id=exercise_id, **validated)
        db.session.add(new_workout_exercise)
        db.session.commit()
        return make_response(workout_exercise_schema.dump(new_workout_exercise), 201)
    except ValidationError as err:
        return make_response(jsonify(err.messages), 400)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)

if __name__ == '__main__':
    app.run(port=5000, debug=True)