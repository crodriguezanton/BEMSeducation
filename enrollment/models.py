from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _

from institution.models import Group
from education.models import Student
from schedule.models import SchoolYear, Semester, Subject


class YearEnroll(models.Model):

    class Meta:
        verbose_name = _('Student Enrollment')
        verbose_name_plural = _('Student Enrollments')

    student = models.ForeignKey(Student)

    school_year = models.ForeignKey(SchoolYear, blank=True, null=True)
    semester = models.ManyToManyField(Semester)

    group = models.ForeignKey(Group, blank=True, null=True)


class StudentStatus(models.Model):
    student = models.OneToOneField(Student)
    group = models.ForeignKey(Group)


class SubjectEnroll(models.Model):

    class Meta:
        verbose_name = _('Subject Enrollment')
        verbose_name_plural = _('Subject Enrollments')

    student = models.ForeignKey(Student)
    semester = models.ManyToManyField(Semester)
    subject = models.ForeignKey(Subject)
