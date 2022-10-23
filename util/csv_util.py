import csv
from component.workout import Workout

def parse_csv(file_name):
    workouts = {}
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Reading {file_name}!')

            else:
                difficulty = int(row[3])
                if difficulty not in workouts.keys():
                    workouts[difficulty] = []

                workouts[difficulty].append(Workout(row[0],row[1],row[2],row[3]))

            line_count += 1
        print(f'Processed {line_count} lines.')
    return workouts