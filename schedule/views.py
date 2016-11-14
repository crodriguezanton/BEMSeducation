from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.generic.dates import DayArchiveView, TodayArchiveView, _date_from_string

from attendance.models import AttendanceEntry
from education.models import Teacher, Student
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
    ordering = 'weekly_timetable_entry__unit__start'

    def dispatch(self, request, *args, **kwargs):
        if not self.kwargs.has_key('year'):
            now = datetime.now()
            self.kwargs['year'] = now.strftime('%Y')
            self.kwargs['month'] = now.strftime('%m')
            self.kwargs['day'] = now.strftime('%d')
        return super(CallView, self).dispatch(request, *args, **kwargs)

    def get_dated_items(self):
        """
        Return (date_list, items, extra_context) for this request.
        """

        year = self.get_year()
        month = self.get_month()
        day = self.get_day()

        date = _date_from_string(year, self.get_year_format(),
                                 month, self.get_month_format(),
                                 day, self.get_day_format())

        return self._get_dated_items(date)

    def get_context_data(self, **kwargs):
        context = super(CallView, self).get_context_data()
        context['page_aside'] = True
        return context

    def get_queryset(self):
        return super(CallView, self).get_queryset().filter(weekly_timetable_entry__teacher=self.request.profile)


@csrf_exempt
def add_entry(request):
    if request.POST.has_key('day'):

        student = Student.objects.get(pk=request.POST.get('student'))
        entryquery = AttendanceEntry.objects.filter(student=student, timetable_entry__pk=request.POST.get('entry'))

        if request.POST.get('status') == 'P':
            if entryquery.count() != 0:
                entryquery.delete()
        else:
            if entryquery.count() != 0:
                entry = entryquery[0]
                entry.type = request.POST.get('status')
            else:
                entry = AttendanceEntry(student=student, timetable_entry = TimetableEntry.objects.get(pk=request.POST.get('entry')), type=request.POST.get('status'))

            entry.save()

        return JsonResponse({'success': True, 'entryquery': entryquery.count()})

    return JsonResponse({'success': False})
