# -*- coding: utf-8 -*-
from __future__ import print_function

from datetime import timedelta
from django.db.models import Q

from education.models import Student, Teacher, Parent, BEMSeducationInstance
from enrollment.models import StudentStatus, YearEnroll
from institution.models import Group, Institution
from schedule.models import Subject, WeeklyTimetableEntry, ClassDay, ClassUnit, SchoolYear, TimetableEntry
from .csv_objects import *


def initBEMS():
    print("\n\nInicialització de BEMS")
    print("======================\n")

    print("Menú principal:\n")
    print("[1]\tInstal·lació completa")

    option = input("\n Escull opció: ")
    base_path = raw_input("\n Introdueix el directori que conté els fitxers .CSV de configuració: ")

    if option is 1:

        instance = BEMSeducationInstance.objects.filter(pk=raw_input("\n Introdueix la instància de BEMS: ")).first()
        institution = Institution.objects.filter(slug=raw_input("\n Introdueix la institució (o None): ")).first()
        school_year = SchoolYear.objects.filter(short_name=raw_input("\n Introdueix el curs escolar: ")).first()

        if instance and school_year:

            import_classrooms(base_path + raw_input("\n Introdueix el nom del fitxer dels AULES: "), instance, institution)
            import_groups(base_path + raw_input("\n Introdueix el nom del fitxer dels GRUPS: "), instance, institution)
            import_teachers(base_path + raw_input("\n Introdueix el nom del fitxer dels TEACHERS: "), instance)
            import_subjects(base_path + raw_input("\n Introdueix el nom del fitxer dels SUBJECTS: "), instance, institution)
            import_timetable(base_path + raw_input("\n Introdueix el nom del fitxer dels TIMETABLE: "), instance, institution)
            import_students(base_path + raw_input("\n Introdueix el nom del fitxer dels ALUMNES: "), instance, school_year)

            print("\n Tot importat! Ja pots començar a utilitzar el BEMS\n\n")


def import_students(path, instance, school_year):

    csv = AlumnesCSV.import_data(data=open(path, "rb"))

    for entry in csv:

        name = entry.name.split(", ")
        gp = entry.grupclasse.split()
        if gp[2] != 'CFPS':
            group = Group.objects.filter(Q(name__contains=gp[0]) & Q(name__contains=gp[1]) & Q(name__contains=gp[2])).first()
        else:
            group = Group.objects.filter(short_name='CFA').first()

        student = Student.objects.create(
            bemsinstance=instance,
            first_name=name[1],
            last_name=name[0],
            address=entry.home
        )

        if entry.resp1 != "":
            name = entry.resp1.split(", ")
            p1 = Parent.objects.create(
                bemsinstance=instance,
                first_name=name[1],
                last_name=name[0],
                contact_email=entry.mail1
            )
            student.responsible.add(p1)

        if entry.resp2 != "":
            name = entry.resp2.split(", ")
            p2 = Parent.objects.create(
                bemsinstance=instance,
                first_name=name[1],
                last_name=name[0],
                contact_email=entry.mail2
            )
            student.responsible.add(p2)

        student.save()

        StudentStatus.objects.create(
            student=student,
            group=group
        )

        YearEnroll.objects.create(
            student=student,
            school_year=school_year,
            group=group
        )

        print('Imported: '+ student.first_name + " " + student.last_name)


def import_classrooms(path, instance, institution=None):
    csv = AulesCSV.import_data(data=open(path, "rb"))

    for entry in csv:

        Classroom.objects.create(
            instance=instance,
            institution=institution,
            name=entry.name,
            short_name=entry.shortName,
            desc=entry.desc
        )

        print('Imported: ' + entry.name)


def import_groups(path, instance, institution=None):
    csv = GrupsCSV.import_data(data=open(path, "rb"))

    for entry in csv:

        Group.objects.create(
            instance = instance,
            institution = institution,
            name = entry.name,
            short_name = entry.shortName,
            classroom = Classroom.objects.filter(short_name=entry.classroom).first()
        )

        print('Imported: ' + entry.name)


def import_teachers(path, instance):
    csv = ProfessorsCSV.import_data(data=open(path, 'rb'))

    for entry in csv:

        Teacher.objects.create(
            bemsinstance = instance,
            shortId = entry.shortId,
            first_name = entry.name,
            last_name = entry.surname
        )

        print('Imported: ' + entry.name + " " + entry.surname)


def import_subjects(path, instance, institution=None):
    csv = MateriesCSV.import_data(data=open(path, 'rb'))

    for entry in csv:

        Subject.objects.create(
            instance=instance,
            institution=institution,
            name = entry.name,
            short_name = entry.shortName,
            default_classroom = Classroom.objects.filter(short_name=entry.defaultClassroom).first()
        )

        print('Imported: ' + entry.name)


def import_timetable(path, instance, institution = None):
    csv = HorarisCSV.import_data(data=open(path, 'rb'))

    for entry in csv:

        WeeklyTimetableEntry.objects.create(
            instance=instance,
            institution=institution,
            group=Group.objects.filter(short_name=entry.group).first(),
            teacher=Teacher.objects.filter(shortId=entry.teacher).first(),
            subject=Subject.objects.filter(short_name=entry.subject).first(),
            classroom=Classroom.objects.filter(short_name=entry.classroom).first(),
            day=ClassDay.objects.filter(instance=instance, institution=institution, day=entry.date).first(),
            unit=ClassUnit.objects.filter(instance=instance, institution=institution, number=entry.time).first()
        )

        print('Imported: ' + entry.subject + " " + str(entry.date) + " " + str(entry.time))


def generate_timetable_entries(semester):

    delta = semester.end - semester.start
    wtes=WeeklyTimetableEntry.objects.all()
    for i in range(delta.days + 1):
        day = semester.start + timedelta(days=i)
        print(day)
        fwtes = wtes.filter(day=ClassDay.objects.filter(day=day.isoweekday()).first())
        for fwte in fwtes:
            print('\t'+fwte.__unicode__())
            TimetableEntry.objects.get_or_create(
                weekly_timetable_entry=fwte,
                date=day,
                active=fwte.class_active(day)
            )