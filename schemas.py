from flask_marshmallow import Marshmallow
from marshmallow import fields, validates, ValidationError

ma = Marshmallow()

class WorkoutSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date()
    duration_seconds = fields.Int(required=True)
    notes = fields.Str()

class ExerciseSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    weight = fields.Float()
    #workout_exercises = fields.Nested('WorkoutExerciseSchema', many=True, exclude=('exercise',))

class WorkoutExerciseSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(required=True)
    sets = fields.Int(required=True)
    duration_seconds = fields.Int(required=True)
    #note = fields.Str()
    #workout_exercises = fields.Nested('WorkoutExerciseSchema', many=True, exclude=('workout',))

    @validates('reps', 'sets', 'duration_seconds')
    def validate_positive_integer(self, value):
        if value <= 0:
            raise ValidationError("Values must be positive integers.")
    

    @validates('duration_seconds')
    def validate_duration_seconds(self, value):
        if value <= 0:
            raise ValidationError("Duration must be a positive integer.")

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)
