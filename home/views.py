from django.http import HttpResponse, JsonResponse

def credits(request):
    content = "Atiq\nRony"
    return HttpResponse(content, content_type="text/plain")

def about(request):
    content = "<h3><i>RiffMates is a collaborative platform for musicians to share and create music together.</i></h3>"
    return HttpResponse(content, content_type="text/html")

def version(request):
    content = "RiffMates v1.0.0"
    return JsonResponse({"version": content})
