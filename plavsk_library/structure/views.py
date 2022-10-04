from django.views.generic import ListView
from content import structure_title
from info.models import Department
from structure.models import Staff


class StaffStructure(ListView):
    model = Staff

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = structure_title
        context['departments'] = Department.objects.all()
        return context
