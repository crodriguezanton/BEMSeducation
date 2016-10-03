from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _

from institution.models import Group
from main.models import Student
from schedule.models import SchoolYear, Semester, Subject, MajorSubject


class YearEnroll(models.Model):

    class Meta:
        verbose_name = _('Student Enrollment')
        verbose_name_plural = _('Student Enrollments')

    student = models.ForeignKey(Student)

    school_year = models.ForeignKey(SchoolYear, blank=True, null=True)
    semester = models.ManyToManyField(Semester)

    group = models.ForeignKey(Group, blank=True, null=True)


class Enroll(models.Model):

    class Meta:
        verbose_name = _('Class Enrollment')
        verbose_name_plural = _('Class Enrollments')

    student = models.ForeignKey(Student)
    semester = models.ManyToManyField(Semester)


class ClassEnroll(Enroll):

    class Meta:
        verbose_name = _('Subject Enrollment')
        verbose_name_plural = _('Subject Enrollments')

    subject = models.ForeignKey(Subject)


class MajorEnroll(Enroll):

    class Meta:
        verbose_name = _('Major Subject Enrollment')
        verbose_name_plural = _('Major Subject Enrollments')

    major = models.ForeignKey(MajorSubject, blank=True, null=True)