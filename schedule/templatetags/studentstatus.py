from django.template import Node, Library, TemplateSyntaxError
from django.utils import six

from education.models import Student
from schedule.models import TimetableEntry

register = Library()


class WithNode(Node):
    def __init__(self, var, name, nodelist, extra_context=None):
        self.nodelist = nodelist
        self.extra_context = extra_context or {}
        self.studentkey = extra_context['student']
        self.tekey = extra_context['te']

    def __repr__(self):
        return "<WithNode>"

    def render(self, context):

        student = context[self.studentkey]
        te = context[self.tekey]
        assert isinstance(student, Student) and isinstance(te, TimetableEntry)
        context['status'] = te.get_student_status(student)
        return self.nodelist.render(context)
        #with context.push(student):
        #    return self.nodelist.render(context)

@register.tag('studentstatus')
def do_with(parser, token, *args):
    """
    Adds one or more values to the context (inside of this block) for caching
    and easy access.

    For example::

        {% with total=person.some_sql_method %}
            {{ total }} object{{ total|pluralize }}
        {% endwith %}

    Multiple values can be added to the context::

        {% with foo=1 bar=2 %}
            ...
        {% endwith %}

    The legacy format of ``{% with person.some_sql_method as total %}`` is
    still accepted.
    """
    bits = token.split_contents()
    remaining_bits = bits[1:]
    extra_context = {
        'student': bits[1],
        'te': bits     [2]
    }
    nodelist = parser.parse(('endstudentstatus',))
    parser.delete_first_token()
    return WithNode(None, None, nodelist, extra_context=extra_context)