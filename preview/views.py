from django.shortcuts import render
from preview.models import Card

# Create your views here.
def index(request):
	context = {}
	return render(request, 'preview/index.html', context)

def all(request):
	runners = Card.objects(side_code='runner', cyclenumber__ne=0)
	runner_identities = runners.filter(type_code='identity')
	runner_events = runners.filter(type_code='event')
	runner_hardwares = runners.filter(type_code='hardware')
	runner_programs = runners.filter(type_code='program')
	context = {
		'runners': runners.to_json(),
		'runner_identities': runner_identities,
		'runner_events': runner_events,
		'runner_hardwares': runner_hardwares,
		'runner_programs': runner_programs
	}
	return render(request, 'preview/all.html', context)