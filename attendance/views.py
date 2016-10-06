# coding=utf-8
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from django_filters.views import FilterView

from attendance.filters import AttendanceEntryFilter, StudentFilter
from attendance.models import AttendanceEntry
from institution.models import Group, Stage, Grade
from main.models import Teacher, Student
from schedule.models import Semester


class AttendanceEntryListView(FilterView, LoginRequiredMixin):
    model = AttendanceEntry
    filterset_class = AttendanceEntryFilter

    def get_context_data(self, **kwargs):
        context = super(AttendanceEntryListView, self).get_context_data(**kwargs)

        context['title'] = "Faltes d'assistència"
        context['description'] = ''
        context['page_aside'] = True

        context['groups'] = Group.objects.all()
        context['stages'] = Stage.objects.all()
        context['grades'] = Grade.objects.all()


        return context

    def get_queryset(self):
        if 'filter' in self.kwargs:
            if self.kwargs['filter'] == 'tutoria':
                return AttendanceEntry.objects.filter(
                    student__group=self.request.bemsprofile.teacher.group_set.all()).all().order_by("-timetable_entry__date")
        else:
            #return AttendanceEntry.objects.filter(teacher=self.request.teacher).all().order_by("-date")
            return AttendanceEntry.objects.all().order_by("-timetable_entry__date")


class RankingListView(FilterView, LoginRequiredMixin):
    model = Student
    template_name = "attendance/ranking_filter.html"
    filterset_class = StudentFilter
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(RankingListView, self).get_context_data(**kwargs)

        context['title'] = 'Castigats'
        context['description'] = ''

        context['groups'] = Group.objects.all()
        context['stages'] = Stage.objects.all()
        context['semesters'] = Semester.objects.all()
        context['grades'] = Grade.objects.all()
        #context['filter'] = self.kwargs.get('filter', 'ALL')
        context['semester'] = self.kwargs.get('semester', '')

        return context

    def student_things(self):

        students = Student.objects.all()

        for student in students:
            if 'semester' in self.kwargs:
                period = Semester.objects.get(short_name=self.kwargs['semester'])
                student.faltes = student.attendanceentry_set.filter(type__char="F",
                                                                    timetable_entry__date__gte=period.start,
                                                                    timetable_entry__date__lte=period.end).count()
                student.justificades = student.attendanceentry_set.filter(type__char="J",
                                                                          timetable_entry__date__gte=period.start,
                                                                          timetable_entry__date__lte=period.end).count()
                student.retards = student.attendanceentry_set.filter(type__char="R",
                                                                     timetable_entry__date__gte=period.start,
                                                                     timetable_entry__date__lte=period.end).count()
                student.consergeria = student.attendanceentry_set.filter(type__char="C",
                                                                         timetable_entry__date__gte=period.start,
                                                                         timetable_entry__date__lte=period.end).count()
                student.total = student.faltes * 3 + student.retards
            else:
                student.faltes = student.attendanceentry_set.filter(type__char="F").count()
                student.justificades = student.attendanceentry_set.filter(type__char="J").count()
                student.retards = student.attendanceentry_set.filter(type__char="R").count()
                student.consergeria = student.attendanceentry_set.filter(type__char="C").count()
                student.total = student.faltes * 3 + student.retards

        return sorted(students, key=lambda t: t.total, reverse=True)

