from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
	return render(request , 'Templates/homepage.html')

def other_page(request):
	firstname = request.POST['FName']
	lastname = request.POST['LName']

	return render(request, 'templates/other_page.html',  {"firstname" : firstname, "lastname": lastname})

@csrf_exempt
def ajax_processor(request):
	v1 = request.POST['data']
	print(v1)
	return JsonResponse({'message' : 'Thank you'})
