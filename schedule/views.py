from django.shortcuts import render
from django.views.generic import TemplateView


class MyTimetableView(TemplateView):
    template_name = "schedule/timetable.html"

    def get_context_data(self, **kwargs):
        context = super(MyTimetableView, self).get_context_data(**kwargs)

        context['title'] = 'El meu horari'
        context['description'] = ''
        context['timetable'] = utils.get_teacher_timetable(Teacher.objects.get(teacherprofile__bemsuser__user=self.request.user))
        context['days'] = ClassDay.objects.filter(institution=Teacher.objects.get(teacherprofile__bemsuser__user=self.request.user).institution)
        context['units'] = ClassUnit.objects.filter(institution=Teacher.objects.get(teacherprofile__bemsuser__user=self.request.user).institution)

        return context