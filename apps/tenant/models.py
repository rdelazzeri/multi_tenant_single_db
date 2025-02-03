from django.db import models
from threading import local
from django.utils.translation import gettext_lazy as _

# Modelo de Tenant
class Tenant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    domain = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



# Armazena o tenant ativo na thread atual
_thread_locals = local()

def get_current_tenant():
    return getattr(_thread_locals, "tenant_id", None)

def set_current_tenant(tenant_id):
    _thread_locals.tenant_id = tenant_id

class TenantQuerySet(models.QuerySet):
    def for_current_tenant(self):
        tenant_id = get_current_tenant()
        if tenant_id:
            return self.filter(tenant_id=tenant_id)
        return self.none()

class TenantManager(models.Manager):
    def get_queryset(self):
        print('dentro do get_queryset')
        return TenantQuerySet(self.model, using=self._db).for_current_tenant()
    
    def get_current_tenant(self):
        tenant_id = get_current_tenant()    
        tenant = Tenant.objects.get(id=tenant_id)
        return tenant



class BaseTenantModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    objects = TenantManager()  # Substitui o manager padrão

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk is not None:
            # Obter o valor original do campo tenant_id do banco de dados
            original = type(self).objects.get(pk=self.pk)
            if original.tenant_id != self.tenant_id:
                raise ValueError("O valor do campo 'tenant_id' não pode ser modificado.")
        else:
            if self.tenant_id is None:
                tenant_id = get_current_tenant()
                self.tenant_id = tenant_id
        super().save(*args, **kwargs)