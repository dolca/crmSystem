from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from crmSystem.views import MyPasswordChangeView, MyPasswordSetView

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('account/password/change/', login_required(MyPasswordChangeView.as_view()), name='account_change_password',),
    path('account/password/set/', login_required(MyPasswordSetView.as_view()), name='account_set_password',),
    path('', include('dashboard.urls')),
    path('listings/', include('listings.urls')),
    path('leads/', include('leads.urls')),
    path('contacts/', include('contacts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'CRM System Administration Panel'
admin.site.site_title = 'CRM System'
admin.site.index_title = 'aPanel'
