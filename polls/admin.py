from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(PostModel)
admin.site.register(PageModel)
admin.site.register(FBAccount)