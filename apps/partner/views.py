from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, DetailView, DeleteView, CreateView, ListView
from .models import Partner
from .forms import PartnerForm

class PartnerCreateView(CreateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'partner/partner_form.html'
    success_url = reverse_lazy('partner:partner_create_success')

class PartnerCreateSuccessView(TemplateView):
    template_name = 'partner/create_success.html'

class PartnersView(ListView):
    model = Partner
    template_name = 'partner/partners_list.html'
    context_object_name = 'partners'

class PartnerEditView(UpdateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'partner/partner_form.html'
    success_url = reverse_lazy('partner:partners_list')

class PartnerReadView(DetailView):
    model = Partner
    template_name = 'partner/partner_detail.html'
    context_object_name = 'partner'

class PartnerDeleteView(DeleteView):
    model = Partner
    template_name = 'partner/partner_confirm_delete.html'
    success_url = reverse_lazy('partner:partners_list')
