from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create users (superheroes)
        self.stdout.write('Creating users...')
        users_data = [
            {'name': 'Tony Stark',      'email': 'tony@avengers.com',    'password': 'ironman123'},
            {'name': 'Steve Rogers',    'email': 'steve@avengers.com',   'password': 'cap123'},
            {'name': 'Thor Odinson',    'email': 'thor@avengers.com',    'password': 'mjolnir123'},
            {'name': 'Bruce Banner',    'email': 'bruce@avengers.com',   'password': 'hulk123'},
            {'name': 'Natasha Romanoff','email': 'natasha@avengers.com', 'password': 'widow123'},
            {'name': 'Bruce Wayne',     'email': 'bruce@wayne.com',      'password': 'batman123'},
            {'name': 'Clark Kent',      'email': 'clark@dailyplanet.com','password': 'superman123'},
            {'name': 'Diana Prince',    'email': 'diana@themyscira.com', 'password': 'wonder123'},
            {'name': 'Barry Allen',     'email': 'barry@ccpd.com',       'password': 'flash123'},
            {'name': 'Hal Jordan',      'email': 'hal@oa.com',           'password': 'greenlantern123'},
        ]
        users = {}
        for u in users_data:
            obj = User.objects.create(**u)
            users[u['name']] = obj

        # Create teams
        self.stdout.write('Creating teams...')
        marvel_members = [
            users['Tony Stark'].name,
            users['Steve Rogers'].name,
            users['Thor Odinson'].name,
            users['Bruce Banner'].name,
            users['Natasha Romanoff'].name,
        ]
        dc_members = [
            users['Bruce Wayne'].name,
            users['Clark Kent'].name,
            users['Diana Prince'].name,
            users['Barry Allen'].name,
            users['Hal Jordan'].name,
        ]
        Team.objects.create(name='Team Marvel', members=marvel_members)
        Team.objects.create(name='Team DC',     members=dc_members)

        # Create activities
        self.stdout.write('Creating activities...')
        activities_data = [
            {'user': 'Tony Stark',       'activity_type': 'Flight Training',   'duration': '60 mins', 'date': date(2024, 1, 15)},
            {'user': 'Steve Rogers',     'activity_type': 'Shield Throwing',   'duration': '45 mins', 'date': date(2024, 1, 16)},
            {'user': 'Thor Odinson',     'activity_type': 'Lightning Workout',  'duration': '90 mins', 'date': date(2024, 1, 17)},
            {'user': 'Bruce Banner',     'activity_type': 'Anger Management',  'duration': '30 mins', 'date': date(2024, 1, 18)},
            {'user': 'Natasha Romanoff', 'activity_type': 'Martial Arts',      'duration': '75 mins', 'date': date(2024, 1, 19)},
            {'user': 'Bruce Wayne',      'activity_type': 'Cape Gliding',      'duration': '50 mins', 'date': date(2024, 1, 20)},
            {'user': 'Clark Kent',       'activity_type': 'Super Speed Run',   'duration': '20 mins', 'date': date(2024, 1, 21)},
            {'user': 'Diana Prince',     'activity_type': 'Lasso Training',    'duration': '60 mins', 'date': date(2024, 1, 22)},
            {'user': 'Barry Allen',      'activity_type': 'Speed Force Sprint', 'duration': '15 mins', 'date': date(2024, 1, 23)},
            {'user': 'Hal Jordan',       'activity_type': 'Ring Construct Drill','duration': '40 mins', 'date': date(2024, 1, 24)},
        ]
        for a in activities_data:
            Activity.objects.create(**a)

        # Create leaderboard
        self.stdout.write('Creating leaderboard...')
        leaderboard_data = [
            {'user': 'Tony Stark',       'score': 980},
            {'user': 'Steve Rogers',     'score': 950},
            {'user': 'Thor Odinson',     'score': 1050},
            {'user': 'Bruce Banner',     'score': 870},
            {'user': 'Natasha Romanoff', 'score': 920},
            {'user': 'Bruce Wayne',      'score': 1000},
            {'user': 'Clark Kent',       'score': 1100},
            {'user': 'Diana Prince',     'score': 970},
            {'user': 'Barry Allen',      'score': 990},
            {'user': 'Hal Jordan',       'score': 860},
        ]
        for lb in leaderboard_data:
            Leaderboard.objects.create(**lb)

        # Create workouts
        self.stdout.write('Creating workouts...')
        workouts_data = [
            {'name': 'Iron Man Cardio',      'description': 'High-intensity suit-powered cardio session.',     'duration': '45 mins'},
            {'name': 'Captain America HIIT', 'description': 'Full-body HIIT inspired by super-soldier serum.', 'duration': '40 mins'},
            {'name': 'Thor Thunder Lifts',   'description': 'Heavy compound lifts worthy of Asgard.',          'duration': '60 mins'},
            {'name': 'Hulk Smash Strength',  'description': 'Maximum strength training – smash everything.',   'duration': '30 mins'},
            {'name': 'Black Widow Combat',   'description': 'Agility-focused martial-arts circuit.',           'duration': '50 mins'},
            {'name': 'Batman Night Run',     'description': 'Endurance run under cover of darkness.',          'duration': '55 mins'},
            {'name': 'Superman Core',        'description': 'Invulnerable core-strengthening routine.',        'duration': '35 mins'},
            {'name': 'Wonder Woman Warrior', 'description': 'Ancient Amazonian warrior conditioning drill.',   'duration': '65 mins'},
            {'name': 'Flash Speed Drills',   'description': 'Lightning-fast agility and speed drills.',        'duration': '20 mins'},
            {'name': 'Green Lantern Yoga',   'description': 'Mind-body willpower yoga for ring wielders.',     'duration': '45 mins'},
        ]
        for w in workouts_data:
            Workout.objects.create(**w)

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated octofit_db with superhero test data!'
        ))
