from marshmallow import Schema, fields, validates, ValidationError

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    name = fields.Str(required=True)
    reps = fields.Int(required=True)
    sets = fields.Int(required=True)
    duration_seconds = fields.Int(required=True)
    exercises = fields.Nested('ExerciseSchema', only=['id', 'name', 'category', 'weight'])

    @validates('reps', 'sets', 'duration_seconds')
    def validate_positive_integer(self, value):
        if value <= 0:
            raise ValidationError("Values must be positive integers.")

    @validates('duration_seconds')
    def validate_duration_seconds(self, value):
        if value <= 0:
            raise ValidationError("Duration must be a positive integer.")

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    weight = fields.Float()
    workout_exercises = fields.Nested('WorkoutExerciseSchema', many=True, exclude=('exercise',))

    @validates('name')
    def validate_name(self, value):
        if not value:
            raise ValidationError("Exercise name cannot be empty.")

    @validates('category')
    def validate_category(self, value):
        if not value:
            raise ValidationError("Exercise category cannot be empty.")

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.DateTime(dump_only=True)
    duration_seconds = fields.Int(required=True)
    note = fields.Str()
    workout_exercises = fields.Nested('WorkoutExerciseSchema', many=True, exclude=('workout',))

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
