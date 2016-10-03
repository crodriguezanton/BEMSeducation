from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.utils.translation import gettext as _

from model_utils.models import TimeFramedModel
from polymorphic.models import PolymorphicModel

from institution.models import Grade, Group, Classroom, Stage
from main.models import BEMSeducationInstance, Teacher, Student
from schedule.constants import DAY_CHOICES


class Semester(TimeFramedModel):

    class Meta:
        verbose_name = _('Semester')
        verbose_name_plural = _('Semesters')

    name = models.CharField(max_length=200)
    instance = models.ForeignKey(BEMSeducationInstance, blank=True, null=True)
    short_name = models.CharField(max_length=6)

    def __unicode__(self):
        return self.name


class SchoolYear(models.Model):

    class Meta:
        verbose_name = _('School Year')
        verbose_name_plural = _('School Years')

    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=6)
    instance = models.ForeignKey(BEMSeducationInstance, blank=True, null=True)
    start = models.DateField()
    end = models.DateField()
    semesters = models.ManyToManyField(Semester)


class Subject(models.Model):

    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')

    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20)
    instance = models.ForeignKey(BEMSeducationInstance, blank=True, null=True)
    default_classroom = models.ForeignKey(Classroom, blank=True, null=True)
    major = models.BooleanField(default=False)

    def __unicode__(self):
        return self.shortName + ": " + self.name


class MajorSubject(models.Model):

    class Meta:
        verbose_name = _('Major Subject')
        verbose_name_plural = _('Major Subjects')

    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=6)
    subject = models.ForeignKey(Subject)
    grade = models.ForeignKey(Grade, blank=True, null=True)
    group = models.ForeignKey(Group, blank=True, null=True)
    teacher = models.ForeignKey(Teacher)

    def __unicode__(self):
        return self.shortName + ": " + self.name + " - " + self.subject.name


class ClassDay(models.Model):

    class Meta:
        verbose_name = _('Class Day')
        verbose_name_plural = _('Class Days')

    instance = models.ForeignKey(BEMSeducationInstance, blank=True, null=True)
    day = models.IntegerField(default=1, choices=DAY_CHOICES)

    def __unicode__(self):
        return self.get_day_display()

    def is_today(self):
        if datetime.today().isoweekday() == self.number:
            return True
        else:
            return False

    @staticmethod
    def get_today():
        if ClassDay.objects.filter(number=datetime.today().isoweekday()).count() != 0:
            return ClassDay.objects.get(number=datetime.today().isoweekday())
        else:
            return None


class ClassUnit(models.Model):

    class Meta:
        verbose_name = _('Class Unit')
        verbose_name_plural = _('Class Units')

    instance = models.ForeignKey(BEMSeducationInstance, blank=True, null=True)
    number = models.IntegerField(default=1)
    days = models.ManyToManyField(ClassDay)
    start = models.TimeField()
    end = models.TimeField()

    def __unicode__(self):
        return self.start.strftime("%H:%M") + " - " + self.end.strftime("%H:%M")

    def is_now(self):
        return self.start <= datetime.now().time() <= self.end

    def is_later(self):
        return self.start > datetime.now().time()

    def is_before(self):
        return self.end < datetime.now().time()

    def is_before_or_current(self):
        return self.start <= datetime.now().time()


class WeeklyTimetableEntry(models.Model):

    class Meta:
        verbose_name = _('Weekly Timetable Entry')
        verbose_name_plural = _('Weekly Timetable Entries')

    group = models.ForeignKey(Group, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, blank=True, null=True)
    subject = models.ForeignKey(Subject, blank=True, null=True)
    classroom = models.ForeignKey(Classroom, blank=True, null=True)
    day = models.ForeignKey(ClassDay)
    unit = models.ForeignKey(ClassUnit)

    def __unicode__(self):
        if self.subject is not None and self.group is not None:
            return self.subject.shortName + " - " + self.group.name + " (" + self.date.name + " " + self.time.__unicode__() + ")"
        else:
            return "(" + self.date.name + " " + self.time.__unicode__() + ")"

    def get_list(self):
        if not self.subject.major:
            students = Student.objects.filter(enroll__classenroll__subject=self.subject, group=self.group).order_by(
                "surname", "name")
        else:
            if self.get_major() is not None:
                students = Student.objects.filter(enroll__majorenroll__major=self.get_major()).order_by("surname",
                                                                                                        "name")
            else:
                students = Student.objects.filter(pk=None)
        return students

    def is_major(self):
        if MajorSubject.objects.filter(subject=self.subject, teacher=self.teacher, group=self.group).count() != 0:
            return True
        else:
            return False

    def get_major(self):
        if not self.is_major():
            return None
        return MajorSubject.objects.get(subject=self.subject, teacher=self.teacher, group=self.group)

    def is_now(self):
        if self.date.is_today() and self.time.is_now():
            return True
        else:
            return False

    def is_later(self):
        return self.time.is_later()

    def is_before(self):
        return self.time.is_before()

    def is_before_or_current(self):
        return self.time.is_before_or_current()

    def class_active(self, day):
        return True #TODO


class TimetableEntry(models.Model):

    class Meta:
        verbose_name = _('Timetable Entry')
        verbose_name_plural = _('Timetable Entry')

    weekly_timetable_entry = models.ForeignKey(WeeklyTimetableEntry, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)


class NonLectivePeriod(PolymorphicModel):
    class Meta:
        verbose_name = _('Non Lective Period')
        verbose_name_plural = _('Non Lective Periods')

    stages = models.ManyToManyField(Stage)
    grades = models.ManyToManyField(Grade)
    groups = models.ManyToManyField(Group)

    def all_institution(self):
        return not (self.stages.count() and self.grades.count() and self.groups.count())


class NonLectiveDay(NonLectivePeriod):

    day = models.DateField()


class NonLectiveHours(NonLectivePeriod):

    start = models.DateTimeField()
    end = models.DateTimeField()


class ClassTrip(NonLectivePeriod):

    start = models.DateTimeField()
    end = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    students = models.ManyToManyField(Student)