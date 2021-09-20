from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models.deletion import CASCADE


class Class_room(models.Model):
    class Meta:
        verbose_name = 'Class_room'
        verbose_name_plural = 'Class_rooms'

    grade = models.PositiveIntegerField()
    message_p = models.TextField(blank=True)

    def __str__(self):
        return str(self.grade)


# class Students(models.Model):
#     class Meta:
#         verbose_name = 'Student'
#         verbose_name_plural = 'Students'
#
#     min_l = MinLengthValidator(8)
#     fio = models.CharField(max_length=250)
#     name = models.CharField(max_length=30)
#     class_room = models.ManyToManyField(Class_room)
#     password = models.CharField(max_length=8, validators=[min_l])
#
#     def __str__(self):
#         return self.fio


class Subject(models.Model):
    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject


class Homework(models.Model):
    class Meta:
        verbose_name = 'Homework'
        verbose_name_plural = 'Homework'

    subject = models.ForeignKey(Subject, on_delete=CASCADE)
    homework = models.TextField()

    def __str__(self):
        return self.homework


class Day(models.Model):
    class Meta:
        verbose_name = 'Day'
        verbose_name_plural = 'Days'

    days = models.CharField(max_length=50)

    def __str__(self):
        return self.days


class Timetable(models.Model):
    class Meta:
        verbose_name = 'Timetable'
        verbose_name_plural = 'Timetable'

    subject = models.ManyToManyField(Subject)
    day = models.ForeignKey(Day, on_delete=CASCADE)
    class_room = models.ForeignKey(Class_room, on_delete=CASCADE)


class MyUser(AbstractUser):
    class Meta:
        verbose_name = 'US'
        verbose_name_plural = 'USS'

    fio = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fio', ]

    def __str__(self):
        return self.fio
