from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta, datetime
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "email": "thundergod@mhigh.edu", "name": "Thor Odinson", "password": "thundergodpassword"},
            {"_id": ObjectId(), "email": "metalgeek@mhigh.edu", "name": "Tony Stark", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "email": "zerocool@mhigh.edu", "name": "Dade Murphy", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "email": "crashoverride@mhigh.edu", "name": "Kate Libby", "password": "crashoverridepassword"},
        ]
        db.users.insert_many(users)

        # Create teams
        teams = [
            {"_id": ObjectId(), "name": "Avengers", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Hackers", "members": [users[2]["_id"], users[3]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "run", "duration": 30, "date": datetime(2025, 4, 30, 8, 0)},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "walk", "duration": 45, "date": datetime(2025, 4, 30, 9, 0)},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "cycle", "duration": 60, "date": datetime(2025, 4, 30, 10, 0)},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "swim", "duration": 25, "date": datetime(2025, 4, 30, 11, 0)},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard
        leaderboard = [
            {"_id": ObjectId(), "team": "Avengers", "points": 150},
            {"_id": ObjectId(), "team": "Hackers", "points": 120},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Pushups", "description": "Do 20 pushups"},
            {"_id": ObjectId(), "name": "Situps", "description": "Do 30 situps"},
            {"_id": ObjectId(), "name": "Jumping Jacks", "description": "Do 50 jumping jacks"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
