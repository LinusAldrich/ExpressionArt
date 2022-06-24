from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Diary)
admin.site.register(Canvas)
admin.site.register(Collage)
