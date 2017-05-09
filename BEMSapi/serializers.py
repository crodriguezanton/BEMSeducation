from rest_framework import serializers

from attendance.models import AttendanceEntry
from education.models import Teacher, Student
from institution.models import Group, Classroom
from schedule.models import TimetableEntry, WeeklyTimetableEntry, Subject, ClassDay, ClassUnit


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('__all__')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('__all__')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('__all__')


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('__all__')

class ClassDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDay
        fields = ('__all__')


class ClassUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassUnit
        fields = ('__all__')


class WeeklyTimetableEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyTimetableEntry
        fields = ('pk', 'group', 'teacher', 'subject', 'classroom', 'day', 'unit')

    group = GroupSerializer()
    teacher = TeacherSerializer()
    subject = SubjectSerializer()
    classroom = ClassroomSerializer()
    day = ClassDaySerializer()
    unit = ClassUnitSerializer()


class TimetableEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimetableEntry
        fields = ('pk', 'weekly_timetable_entry', 'date', 'active')

    weekly_timetable_entry = WeeklyTimetableEntrySerializer()


class AttendanceEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceEntry
        fields = ('pk', 'type', 'created', 'modified')


class StudentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('pk', 'first_name', 'last_name', 'bemsuser', 'status')

    status = AttendanceEntrySerializer(read_only=True)
