from django.urls import path

from addressapp.views import address_query, address_add, address_edit, address_delete

app_name = 'addressapp'

urlpatterns = [
    path('query/', address_query),
    path('add/', address_add),
    path('edit/', address_edit),
    path('delete/', address_delete)
]
