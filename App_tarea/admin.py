from django.contrib import admin
from App_tarea.models import Topic, Webpage, AccessRecord, Eras

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(Eras)