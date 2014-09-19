from django.shortcuts import render
from preview.models import Card

# Create your views here.
def index(request):
	context = {}
	return render(request, 'preview/index.html', context)

def all(request):
	card_list = Card.objects.all().order_by('code')
	context = { 'card_list': card_list}
	return render(request, 'preview/all.html', context)