from django.views.generic import ListView
from structure.models import Staff, Department


class StaffStructure(ListView):
    model = Staff

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Department'] = Department.objects.all()
        return context
