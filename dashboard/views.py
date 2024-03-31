from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class DashboardView(LoginRequiredMixin, TemplateView):
    pass


dashboard_view = DashboardView.as_view(template_name='dashboard/dashboard.html')
