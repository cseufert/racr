from django.db import models
from django.contrib.auth.models import User as AuthUser


class FieldResult(models.Model):
    user = models.ForeignKey(AuthUser)
    event = models.ForeignKey('Event')
    result = models.IntegerField()


class TrackResult(models.Model):
    user = models.ForeignKey(AuthUser)
    event = models.ForeignKey('Event')
    heat = models.IntegerField()
    lane = models.IntegerField()
    time = models.IntegerField()


class ParticipateResult(models.Model):
    user = models.ForeignKey(AuthUser)
    event = models.ForeignKey('Event')


class Event(models.Model):
    TYPE_CHOICES = (
        (1, 'TrackLanes'),
        (2, 'TrackFinish'),
        (3, 'Field'),
        (4, 'Participation'),
    )

    name = models.TextField()
    type = models.SmallIntegerField(choices=TYPE_CHOICES)
    age_group = models.ForeignKey('AgeGroup')
    meet = models.ForeignKey('Meet')
    event_class = models.ForeignKey('EventClass')
    created_by = models.ForeignKey(AuthUser)


class MeetEvent(models.Model):
    event = models.ForeignKey('Event')
    meet = models.ForeignKey('Meet')


class Meet(models.Model):
    name = models.TextField()
    meet_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(AuthUser)


class PointsMap(models.Model):
    meet = models.ForeignKey('Meet')
    event_class = models.ForeignKey('EventClass')
    count = models.IntegerField()
    place = models.IntegerField()
    recurring = models.BooleanField()


class EventClass(models.Model):
    name = models.TextField()


class EventRecord(models.Model):
    TYPE_CHOICES = (
        (1, 'World'),
        (2, 'Australian'),
        (3, 'Region'),
    )

    type = models.SmallIntegerField(choices=TYPE_CHOICES)
    event_time = models.IntegerField()
    age_group = models.ForeignKey('AgeGroup')
    date = models.DateTimeField()


class House(models.Model):
    name = models.TextField()
    total_points = models.IntegerField()


class User(models.Model):
    GENDER_CHOICES = (
        (1, 'Female'),
        (2, 'Male'),
    )

    TYPE_CHOICES = (
        (1, 'Student'),
        (2, 'Staff'),
        (3, 'Marshall'),
    )

    user = models.OneToOneField(AuthUser)
    total_points = models.IntegerField()
    dob = models.DateTimeField()
    house = models.ForeignKey('House')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES)
    form_group = models.CharField(max_length=5)
    type = models.SmallIntegerField(choices=TYPE_CHOICES)
    school = models.ForeignKey('School')


class School(models.Model):
    name = models.TextField()
    created_by = models.ForeignKey(User, related_name='created_by')


class AgeGroup(models.Model):
    name = models.TextField()
    total_points = models.IntegerField()
    total_points_male = models.IntegerField()
    total_points_female = models.IntegerField()
    max_age = models.IntegerField()