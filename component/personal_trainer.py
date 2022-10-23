import pause
import random
from datetime import datetime

class PersonalTrainer:
    def __init__(self, workouts, max_workout_points):
        self.workouts = workouts
        self.max_workout_points = max_workout_points


    def print_workouts(self):
        for key in self.workouts:
            for workout in self.workouts[key]:
                workout.print_info()

    def workout(self):
        #TODO pause until the thirty minute mark of the hour, then create a pop up with the current workout plan

        #Creating workout plan
        #current_workout_points is the total number of points for this session's workout
        current_workout_points = random.randint(1,self.max_workout_points)
        print(f'This session is going to be worth {current_workout_points} points!')

        workout_plan = []
        while (current_workout_points >= 1):
            #current difficulty is the difficulty of the current exercise to be added to the plan
            current_difficulty = random.randint(1,current_workout_points)
            print(f"Let's pick a workout that is level {current_difficulty}!")
            workout = random.choice(self.workouts[current_difficulty])
            print(f"Looks like we're going to do some {workout.name}!")
            workout_plan.append(workout)
            current_workout_points -= current_difficulty

        print("Here's our current workout plan:")
        for workout in workout_plan:
            workout.print_info()