from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext as _
from wheel.signatures.djbec import B

from education.models import Teacher, BEMSeducationInstance


class Institution(models.Model):
    class Meta:
        verbose_name = _('Institution')
        verbose_name_plural = _('Institutions')

    instance = models.ForeignKey(BEMSeducationInstance)
    name = models.CharField(max_length=200)
    slug = models.SlugField(primary_key=True)


class Stage(models.Model):

    class Meta:
        verbose_name = _('Stage')
        verbose_name_plural = _('Stages')

    instance = models.ForeignKey(BEMSeducationInstance)
    institution = models.ForeignKey(Institution, blank=True, null=True)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=6)

    def __unicode__(self):
        return self.name


class Grade(models.Model):

    class Meta:
        verbose_name = _('Grade')
        verbose_name_plural = _('Grades')

    instance = models.ForeignKey(BEMSeducationInstance)
    institution = models.ForeignKey(Institution, blank=True, null=True)
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=6)
    stage = models.ForeignKey(Stage)

    def __unicode__(self):
        return self.name


class Classroom(models.Model):

    class Meta:
        verbose_name = _('Classroom')
        verbose_name_plural = _('Classrooms')

    instance = models.ForeignKey(BEMSeducationInstance)
    institution = models.ForeignKey(Institution, blank=True, null=True)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    building = models.CharField(max_length=200)
    floor = models.CharField(max_length=50)
    desc = models.CharField(max_length=300, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Group(models.Model):

    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')

    instance = models.ForeignKey(BEMSeducationInstance)
    institution = models.ForeignKey(Institution, blank=True, null=True)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20)
    tutor = models.ForeignKey(Teacher, blank=True, null=True)
    grade = models.ForeignKey(Grade, blank=True, null=True)
    classroom = models.ForeignKey(Classroom, blank=True, null=True)

    def __unicode__(self):
        return self.name