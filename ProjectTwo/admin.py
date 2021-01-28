from django.contrib import admin

from .models import (RequestType, State, Status, UserDetails, UserRequest,)
# Register your models here.

admin.site.register(RequestType)
admin.site.register(State)
admin.site.register(Status)
admin.site.register(UserDetails)
admin.site.register(UserRequest)