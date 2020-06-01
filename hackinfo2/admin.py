from django.contrib import admin

# Register your models here.
from .models import Organiser
admin.site.register(Organiser)

from .models import Userdata
admin.site.register(Userdata)

from .models import LeaderDetail
admin.site.register(LeaderDetail)
