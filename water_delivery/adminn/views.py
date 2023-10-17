from django.views.generic import TemplateView
from .models import *

class DashboardView(TemplateView):
    template_name = 'adminn/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dashboard_data = DashboardData.objects.first()
        context['dashboard_data'] = dashboard_data

        return context