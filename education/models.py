from __future__ import unicode_literals

from BEMSauth.models import BEMSProfile

from BEMSinstances.models import BEMSInstance
from django.db import models
from django.utils.translation import gettext as _


class BEMSeducationInstance(BEMSInstance):

    class Meta:
        verbose_name = _('BEMS.education Instance')
        verbose_name_plural = _('BEMS.education Instances')

    code = models.CharField(max_length=10)


class Parent(BEMSProfile):

    class Meta:
        verbose_name = _("Parent Profile")
        verbose_name_plural = _("Parent Profiles")

    contact_email = models.EmailField(blank=True, null=True)

    @staticmethod
    def get_profile_name():
        return _("Parent")


class Student(BEMSProfile):

    class Meta:
        verbose_name = _("Student Profile")
        verbose_name_plural = _("Student Profiles")

    address = models.TextField(blank=True, null=True)
    responsible = models.ManyToManyField(Parent, blank=True)

    @staticmethod
    def get_profile_name():
        return _("Student")


class Teacher(BEMSProfile):

    class Meta:
        verbose_name = _("Teacher Profile")
        verbose_name_plural = _("Teacher Profiles")

    @staticmethod
    def get_profile_name():
        return _("Teacher")