from csvImporter.fields import CharField, IgnoredField, IntegerField
from csvImporter.model import CsvModel
from institution.models import Classroom


class AulesCSV(CsvModel):
    shortName = CharField()
    name = CharField()
    s1 = IgnoredField()
    s2 = IgnoredField()
    s3 = IgnoredField()
    s4 = IgnoredField()
    s5 = IgnoredField()
    s6 = IgnoredField()
    s7 = IgnoredField()
    s8 = IgnoredField()
    s9 = IgnoredField()
    desc = CharField()
    ss1 = IgnoredField()
    ss2 = IgnoredField()
    ss3 = IgnoredField()
    ss4 = IgnoredField()
    ss5 = IgnoredField()

    class Meta:
        delimiter = ","
        dbModel = Classroom


class GrupsCSV(CsvModel):
    shortName = CharField()
    name = CharField()
    ss1 = IgnoredField()
    classroom = CharField()
    s0 = IgnoredField()
    s1 = IgnoredField()
    s2 = IgnoredField()
    s3 = IgnoredField()
    s4 = IgnoredField()
    s5 = IgnoredField()
    s6 = IgnoredField()
    s7 = IgnoredField()
    s8 = IgnoredField()
    s9 = IgnoredField()
    a0 = IgnoredField()
    a1 = IgnoredField()
    a2 = IgnoredField()
    a3 = IgnoredField()
    a4 = IgnoredField()
    a5 = IgnoredField()
    a6 = IgnoredField()
    a7 = IgnoredField()
    a8 = IgnoredField()
    a9 = IgnoredField()
    b0 = IgnoredField()
    b1 = IgnoredField()
    b2 = IgnoredField()
    b3 = IgnoredField()
    b4 = IgnoredField()
    b5 = IgnoredField()
    b6 = IgnoredField()

    class Meta:
        delimiter = ","


class ProfessorsCSV(CsvModel):
    shortId = CharField()
    surname = CharField()
    s0 = IgnoredField()
    s1 = IgnoredField()
    s2 = IgnoredField()
    s3 = IgnoredField()
    s4 = IgnoredField()
    s5 = IgnoredField()
    s6 = IgnoredField()
    s7 = IgnoredField()
    s8 = IgnoredField()
    s9 = IgnoredField()
    a0 = IgnoredField()
    a1 = IgnoredField()
    a2 = IgnoredField()
    a3 = IgnoredField()
    a4 = IgnoredField()
    a5 = IgnoredField()
    a6 = IgnoredField()
    a7 = IgnoredField()
    position = CharField()
    b1 = IgnoredField()
    desc = CharField()
    ss0 = IgnoredField()
    ss1 = IgnoredField()
    ss2 = IgnoredField()
    ss3 = IgnoredField()
    ss4 = IgnoredField()
    name = CharField()
    c0 = IgnoredField()
    c1 = IgnoredField()
    c2 = IgnoredField()
    c3 = IgnoredField()
    c4 = IgnoredField()
    c5 = IgnoredField()
    c6 = IgnoredField()
    c7 = IgnoredField()
    c8 = IgnoredField()
    c9 = IgnoredField()
    z0 = IgnoredField()
    z1 = IgnoredField()
    z2 = IgnoredField()

    class Meta:
        delimiter = ","


class MateriesCSV(CsvModel):
    shortName = CharField()
    name = CharField()
    b1 = IgnoredField()
    defaultClassroom = CharField()
    s0 = IgnoredField()
    s1 = IgnoredField()
    s2 = IgnoredField()
    s3 = IgnoredField()
    s4 = IgnoredField()
    s5 = IgnoredField()
    s6 = IgnoredField()
    s7 = IgnoredField()
    s8 = IgnoredField()
    s9 = IgnoredField()
    a0 = IgnoredField()
    a1 = IgnoredField()
    a2 = IgnoredField()
    a3 = IgnoredField()
    a4 = IgnoredField()
    a5 = IgnoredField()
    a6 = IgnoredField()

    class Meta:
        delimiter = ","


class HorarisCSV(CsvModel):
    a1 = IgnoredField()
    group = CharField()
    teacher = CharField()
    subject = CharField()
    classroom = CharField()
    date = IntegerField()
    time = IntegerField()
    b1 = IgnoredField()

    class Meta:
        delimiter = ","


class AlumnesCSV(CsvModel):
    id = IntegerField()
    name = CharField()
    plaest = CharField()
    niv = CharField()
    gpscls = CharField()
    grupclasse = CharField()
    email = CharField()
    home = CharField()
    mbl1 = CharField()
    mail1 = CharField()
    resp1 = CharField()
    resp2 = CharField()
    tlf2 = CharField()
    mbl2 = CharField()
    mail2 = CharField()

    class Meta:
        delimiter = ","
        has_header = True

class Alumnes2CSV(CsvModel):
    row = CharField()

    class Meta:
        delimiter = ","
        has_header = True


class ModalitatsCSV(CsvModel):
    name = CharField()
    BLOC1 = CharField()
    BLOC2 = CharField()
    BLOC3 = CharField()
    BLOC4 = CharField()

    class Meta:
        delimiter = ';'


class RodesCSV(CsvModel):
    s1 = CharField()
    s2 = CharField()
    n = CharField()
    roda = CharField()

    class Meta:
        delimiter = ';'