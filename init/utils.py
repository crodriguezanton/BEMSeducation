# -*- coding: utf-8 -*-
from __future__ import print_function
from education.models import Student
from .csv_objects import *


def initBEMS():
    print("\n\nInicialització de BEMS")
    print("======================\n")

    print("Menú principal:\n")
    print("[1]\tInstal·lació completa")

    option = input("\n Escull opció: ")
    base_path = raw_input("\n Introdueix el directori que conté els fitxers .CSV de configuració: ")

    if option is 1:

        import_students(base_path + raw_input("\n Introdueix el nom del fitxer dels ALUMNES: "))

        print("\n Tot importat! Ja pots començar a utilitzar el BEMS\n\n")


def import_students(path):

    csv = AlumnesCSV.import_data(data=open(path, "rb"))

    groups = get_groups(csv)
    grades = get_grades(csv)
    stages = get_stages(csv)

    print(groups)
    print(grades)
    print(stages)


def get_groups(csv):
    groups = set()

    for entry in csv:
        groups = groups.union({entry.grupclasse})

    return groups


def get_grades(csv):
    grades = set()

    for entry in csv:
        grades = grades.union({entry.niv})

    return grades


def get_stages(csv):
    stages = set()

    for entry in csv:
        stages = stages.union({entry.plaest})

    return stages