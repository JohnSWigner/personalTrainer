from util import csv_util
from component.personal_trainer import PersonalTrainer

# TODO make this configuration driven
def main():
    max_workout_points = 3
    workouts = csv_util.parse_csv('config/workouts.csv')
    #TODO configure workout schedule
    trainer = PersonalTrainer(workouts, max_workout_points)
    trainer.workout()

if __name__ == '__main__':
    main()