from django.urls import path
from . import views as v
from .views import *

app_name = 'partner'

urlpatterns = [
    path('partner/create', PartnerCreateView.as_view(), name='partner_create'),
    path('partner/create-success/', PartnerCreateSuccessView.as_view(), name='partner_create_success'),
    path('partners/', PartnersView.as_view(), name='partners_list'),
    path('partner/<int:pk>/edit', PartnerEditView.as_view(), name='partner_edit'),
    path('partner/<int:pk>/detail', PartnerReadView.as_view(), name='partner_detail'),
    path('partner/<int:pk>/delete', PartnerDeleteView.as_view(), name='partner_delete'),


]

