# URLconf
from django.urls import path

from .views import (Register, Login, Request, GetMasterTableDetails, GetRequestById, UserAllRequests,)

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('request/', Request.as_view()),
    path('user_all_requests/<int:user_id>/', UserAllRequests.as_view()),
    path('request_by_id/<int:request_id>/', GetRequestById.as_view()),
    path('master_data/', GetMasterTableDetails.as_view()),
]