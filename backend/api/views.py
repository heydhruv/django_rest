from django.http import JsonResponse

res = {"Greetings":"Hey there !"}
def home_api(request, *args, **kwargs):
    return JsonResponse(res)