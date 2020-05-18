import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Account



class SignUpView(View):
    def post(self, request):

        data = json.loads(request.body)

        try:
            if Account.objects.filter(email=data['email']).exists():
                return JsonResponse({'message':'EMAIL_ALREADY_EXISTS'},status=400)
            else:
                Account.objects.create(
                        email = data['email'],
                        password = data['password'],
                )
                return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status=400)


class SignInView(View):
    def post(self, request):

        data = json.loads(request.body)

        try:
            if Account.objects.filter(email = data['email']).exists():
                if data['password'] == Account.objects.get(email = data['email']).password:
                    return HttpResponse(status=200)
                return JsonResponse({'message':'INVALID_USER'},status=401)
            return HttpResponse(status=401)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status=400)

                        

