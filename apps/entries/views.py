from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.views.generic import TemplateView
from .models import Entry
# Create your views here.
class IndexView(TemplateView):

	template_name = 'index.html'

class IndexView2(TemplateView):

	template_name = 'index2.html'


def my_ajax(request):
	print request.POST
	entries = list(Entry.objects.all().values('title','content'))
	return JsonResponse(entries, safe=False)

def save_entry(request):
	if request.is_ajax():
		Entry.objects.create(title = request.POST['title'],
			content = request.POST['content'])
		return JsonResponse({'message' : 'Se creo correctamente'})
	else:
		raise Http404