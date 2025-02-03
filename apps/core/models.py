from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.tenant.models import Tenant
from .managers import CustomUserManager

# Create your models here.
# Modelo de Usuário Personalizado
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    tenants = models.ManyToManyField(Tenant, through='UserTenant')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    groups = models.ManyToManyField(
        Group,
        related_name='core_user_set',  # Change related_name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='core_user_permissions_set',  # Change related_name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    objects = CustomUserManager()

# Modelo de Associação entre Usuário e Tenant
class UserTenant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'tenant')