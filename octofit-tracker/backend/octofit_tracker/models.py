from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    class Meta:
        db_table = 'users'

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=User)
    class Meta:
        db_table = 'teams'

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateTimeField()
    class Meta:
        db_table = 'activity'

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table = 'workouts'
