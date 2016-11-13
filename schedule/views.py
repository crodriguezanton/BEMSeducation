from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from education.models import Teacher
from schedule.models import TimetableEntry, ClassUnit, ClassDay


class TimetableView(TemplateView):
    pass


class MyTimetableView(TimetableView):
    template_name = "schedule/timetable.html"

    def get_context_data(self, **kwargs):
        context = super(MyTimetableView, self).get_context_data(**kwargs)

        context['title'] = 'El meu horari'
        context['description'] = ''
        # context['timetable'] = utils.get_teacher_timetable(Teacher.objects.get(teacherprofile__bemsuser__user=self.request.user))
        context['days'] = ClassDay.objects.filter(
            institution=Teacher.objects.get(teacherprofile__bemsuser__user=self.request.user).institution)
        context['units'] = ClassUnit.objects.filter(
            institution=Teacher.objects.get(teacherprofile__bemsuser__user=self.request.user).institution)

        return context


class CallView(DayArchiveView):
    model = TimetableEntry
    date_field = 'date'
    allow_future = True
    allow_empty = False
    month_format = '%m'

    def get_context_data(self, **kwargs):
        context = super(CallView, self).get_context_data()
        context['page_aside'] = True
        return context

    def get_queryset(self):
        return super(CallView, self).get_queryset().filter(weekly_timetable_entry__teacher=self.request.profile)


class TodayCallView(TodayArchiveView):
    model = TimetableEntry
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super(TodayCallView, self).get_context_data()
        context['page_aside'] = True
        return context

    def get_queryset(self):
        return super(TodayCallView, self).get_queryset().filter(weekly_timetable_entry__teacher=self.request.profile)
