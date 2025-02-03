from django.db import models
from apps.tenant.models import BaseTenantModel

class Partner(BaseTenantModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name