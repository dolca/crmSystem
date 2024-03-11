from django.views.generic import TemplateView


class LayoutsView(TemplateView):
    pass


horizontal_layout = LayoutsView.as_view(template_name="layouts/horizontal.html")
detached_layout = LayoutsView.as_view(template_name="layouts/detached.html")
two_column_layout = LayoutsView.as_view(template_name="layouts/two_column.html")
vertical_hovered_layout = LayoutsView.as_view(template_name="layouts/vertical_hovered.html")
