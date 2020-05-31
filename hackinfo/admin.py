from django.contrib import admin

# Register your models here.
from .models import SignUpDetail
admin.site.register(SignUpDetail)

from .models import LeaderDetail
admin.site.register(LeaderDetail)
