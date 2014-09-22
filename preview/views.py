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

def tables(request):
	cards = Card.objects(cyclenumber__ne=0)
	runners = cards.filter(side_code='runner')
	runner_identities = runners.filter(type_code='identity')
	runner_events = runners.filter(type_code='event')
	runner_hardwares = runners.filter(type_code='hardware')
	runner_programs = runners.filter(type_code='program')

	corps = cards.filter(side_code='corp')
	corp_identities = corps.filter(type_code='identity')
	corp_agendas = corps.filter(type_code='agenda')
	corp_operations = corps.filter(type_code='operation')
	corp_assets = corps.filter(type_code='asset')
	corp_upgrades = corps.filter(type_code='upgrade')
	corp_ices = corps.filter(type_code='ice')

	context = {
		'cards': cards.to_json(),
		'runners': runners.to_json(),
		'runner_identities': runner_identities.to_json(),
		'runner_events': runner_events.to_json(),
		'runner_hardwares': runner_hardwares.to_json(),
		'runner_programs': runner_programs.to_json(),
		'corps': corps.to_json(),
		'corp_identities': corp_identities.to_json(),
		'corp_agendas': corp_agendas.to_json(),
		'corp_operations': corp_operations.to_json(),
		'corp_assets': corp_assets.to_json(),
		'corp_upgrades': corp_upgrades.to_json(),
		'corp_ices': corp_ices.to_json()
	}
	return render(request, 'preview/table.html', context)