from django.urls import path
from layouts import views

app_name = 'layouts'

urlpatterns = [
    path('horizontal', views.horizontal_layout, name='horizontal'),
    path('detached', views.detached_layout, name='detached'),
    path('two-column', views.two_column_layout, name='two_column'),
    path('vertical-hovered', views.vertical_hovered_layout, name='vertical_hovered'),
]
