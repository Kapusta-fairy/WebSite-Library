from django.views.generic import ListView
from content import info_title, full_name, short_name, date_creation, leader, organization_type, founder, \
    legal_address, actual_address
from info.models import Department


class OrganizationInfo(ListView):
    model = Department

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = info_title
        context['full_name'] = full_name
        context['short_name'] = short_name
        context['date_creation'] = date_creation
        context['leader'] = leader
        context['organization_type'] = organization_type
        context['founder'] = founder
        context['legal_address'] = legal_address
        context['actual_address'] = actual_address
        return context
