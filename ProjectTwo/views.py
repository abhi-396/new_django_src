from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (RequestType, State, Status, UserDetails, UserRequest,)

# Create your views here.

class Register(APIView):
    def post(self, request):
        try:
            user = UserDetails(name=request.data["name"], email=request.data["email"],
                                phone=request.data["phone"], password=request.data["password"])
            user.save()
            response = Response({"Message": "Success"}, status=status.HTTP_200_OK)
            return response
        except Exception as e:
            return Response(str(e), status=status.HTTP_200_OK)

class Login(APIView):
    def post(self, request):
        try:
            user = UserDetails.objects.get(email=request.data["email"], password=request.data["password"])
            obj = {
                "id": user.id,
                "email": user.email
            }
            response = Response(obj, status=status.HTTP_200_OK)
            return response
        except Exception as e:
            return Response(str(e), status=status.HTTP_200_OK)        

class GetMasterTableDetails(APIView):
    def get(self, request):
        try:
            request_type=RequestType.objects.all()
            request_type_obj=[]
            if len(request_type)>0:
                for data in request_type:
                    obj = {
                        "id": data.id,
                        "name": data.name
                    }
                    request_type_obj.append(obj)

            state=State.objects.all()
            state_obj=[]
            if len(state)>0:
                for data in state:
                    obj = {
                        "id": data.id,
                        "name": data.name
                    }
                    state_obj.append(obj)

            status=Status.objects.all()
            status_obj=[]
            if len(status)>0:
                for data in status:
                    obj = {
                        "id": data.id,
                        "status": data.status
                    }
                    status_obj.append(obj)

            obj = {
                'request_type': request_type_obj,
                'state': state_obj,
                'status': status_obj
            }

            return Response(obj)
        except Exception as e:
            return Response(str(e))

class Request(APIView):
    def post(self, request):
        try:
            request_state = State.objects.get(id=request.data["state_id"])
            updated_by = UserDetails(id=request.data["user_id"])
            request_status = Status.objects.get(id=1)
            user_request = UserRequest(request_type=request.data["request_type"], request_state=request_state,
            updated_by=updated_by, request_desc=request.data["description"], request_city=request.data["city"], 
            request_pincode=request.data["pincode"], alternate_phone=request.data['alternate_phone'], status=request_status)
            user_request.save()
            return Response({"Message": "Success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_200_OK)
    def put(self, request):
        try:
            user_request = UserRequest.objects.get(id=request.data['id'])
            status = Status.objects.get(id=request.data["status_id"])
            user_request.status = status
            user_request.remarks = request.data["remark"]
            user_request.save
            return Response({"Message": "Success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_200_OK)            


class UserAllRequests(APIView):
    def get(self, request, user_id):
        try:
            user = UserDetails.objects.get(id=user_id)
            user_request = UserRequest.objects.filter(updated_by=user)
            response = []
            for data in user_request:
                obj = {
                    "id": data.id,
                    "request_type": data.request_type,
                    "request_desc": data.request_desc,
                    "request_city": data.request_city,
                    "request_state": data.request_state.name,
                    "request_pincode": data.request_pincode,
                    "alternate_phone": data.alternate_phone,
                    "status": data.status.status,
                    "remarks": data.remarks,
                    "updated_by": data.updated_by.name,
                    "date_time": data.date_time
                }
                response.append(obj)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_200_OK)

class GetRequestById(APIView):
    def get(self, request, request_id):
        try:
            user_request = UserRequest.objects.get(id=request_id)
            obj = {
                "id": user_request.id,
                "request_type": user_request.request_type,
                "request_desc": user_request.request_desc,
                "request_city": user_request.request_city,
                "request_state": user_request.request_state.name,
                "request_pincode": user_request.request_pincode,
                "alternate_phone": user_request.alternate_phone,
                "status": user_request.status.status,
                "remarks": user_request.remarks,
                "updated_by": user_request.updated_by.name
            }
            return Response(obj, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_200_OK)
