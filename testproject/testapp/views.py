from django.shortcuts import render
# Create your views here.
from .models import struct, team
def home(request):
    obj1 = struct.objects.all()
    obj2 = team.objects.all()
    return render(request, 'index.html', {'place': obj1, 'creator': obj2})
#def result(request):
#   x=int(request.POST['num1'])
#   y=int(request.POST['num2'])
#   adds=x+y
#   subs=x-y
#   mult=x*y
#   if y!=0:
#     divis=x/y
#   else:
#     return HttpResponse("error division by zero")
#   return render(request,'result.html',{'addition':adds,'substract':subs,'multiply':mult,'division':divis})

