from django.contrib import admin
from django.apps import apps

# Get all models from the current app
app = apps.get_app_config('core')

# Register each model with the admin site
for model in app.get_models():
    admin.site.register(model)
