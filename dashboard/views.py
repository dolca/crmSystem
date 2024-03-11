from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    pass


dashboard_view = DashboardView.as_view(template_name="dashboard/dashboard.html")
