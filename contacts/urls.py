from django.urls import path
from contacts.views import ContactCreateView, CreateContactDoneView, ContactListView, ContactUpdateView, \
    ContactDeleteView, DeleteContactDoneView, ContactDetailView, check_duplicate, save_contact, get_contact_details

app_name = 'contacts'

urlpatterns = [
    path('add-contact', ContactCreateView.as_view(), name='add_contact'),
    path('contact-added', CreateContactDoneView.as_view(), name='contact_added'),
    path('all-contacts', ContactListView.as_view(), name='contacts_list'),
    path('edit-contact/<int:pk>', ContactUpdateView.as_view(), name='edit_contact'),
    path('delete-contact/<int:pk>', ContactDeleteView.as_view(), name='delete_contact'),
    path('contact-deleted', DeleteContactDoneView.as_view(), name='contact_deleted'),
    path('contact-details/<int:pk>', ContactDetailView.as_view(), name='contact_details'),

    path('api/check-duplicate/', check_duplicate, name='check_duplicate'),
    path('api/save-contact/', save_contact, name='save_contact'),
    path('api/contact-details/<int:contact_id>', get_contact_details, name='get_contact_details'),
]
