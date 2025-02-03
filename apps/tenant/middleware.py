from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.conf import settings
from .models import set_current_tenant
from django.urls import reverse_lazy

class TenantMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        tenant_id = request.session.get('tenant_id')
        print(f'path: {request.path} - tenant: {tenant_id}')

        if not tenant_id and request.path not in settings.BY_PASS_TENANT:
            redirect_url = reverse_lazy(settings.LOGIN_URL[0])
            print(f'{request.path} not in {settings.BY_PASS_TENANT} redirecting to: {redirect_url}')
            return redirect(redirect_url)
        
        request.tenant_id = tenant_id
        set_current_tenant(tenant_id)
        return self.get_response(request)


    def process_request(self, request):
        tenant_id = request.session.get('tenant_id')
        print(settings.LOGIN_URL)
        if not tenant_id and request.path not in settings.LOGIN_URL:
            return redirect(settings.LOGIN_URL[0])
        request.tenant_id = tenant_id
        set_current_tenant(tenant_id)