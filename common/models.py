from mongoengine import *
from mongoengine.queryset import QuerySet

# Create your models here.
class CardQuerySet(QuerySet):
	# filter helpers
	def type_filter(self, param):
		return self.filter(type_code=param)

	def subtype_filter(self, param):
		return self.filter(subtype_code=param)

	def faction_filter(self, param):
		return self.filter(faction_code=param)

	## side filters
	def runner_cards(self):
		return self.filter(side_code='runner')

	def corp_cards(self):
		return self.filter(side_code='corp')

	## faction filters
	def shapers():
		faction_filter('shaper')

	def criminals():
		faction_filter('criminal')

	def jintekis():
		faction_filter('jinteki')

	def haas_bioroids():
		faction_filter('haas-bioroid')

	def neutrals():
		faction_filter('neutral')

	def weyland_consortiums():
		faction_filter('weyland-consortium')

	def anarchs():
		faction_filter('anarch')

	def nbns():
		faction_filter('nbn')

	## type filters
	def agendas():
		type_filter('agenda')

	def assets():
		type_filter('asset')

	def events():
		type_filter('event')

	def hardwares():
		type_filter('hardware')

	def ices():
		type_filter('ice')

	def identities():
		type_filter('identity')

	def operations():
		type_filter('operation')

	def programs():
		type_filter('program')

	def resources():
		type_filter('resource')

	def upgrades():
		type_filter('upgrades')

class AbstractCard(Document):
	advancementcost = IntField()
	agendapoints = IntField()
	baselink = IntField()
	card_type = StringField()
	code = StringField()
	cost = IntField()
	cyclenumber = IntField()
	faction = StringField()
	faction_code = StringField()
	faction_letter = StringField()
	faction_cost = IntField()
	flavor = StringField()
	illustrator = StringField()
	influence_limit = IntField()
	limited = BooleanField()
	memoryunits = IntField()
	minimumdecksize = IntField()
	number = IntField()
	set_code = StringField()
	setname = StringField()
	side = StringField()
	side_code = StringField()
	strength = IntField()
	subtype = StringField()
	subtype_code = StringField()
	text = StringField()
	title = StringField()
	type_code = StringField()
	uniqueness = BooleanField()
	imagesrc = StringField()

	meta = {
		'abstract': True,
		'ordering': ['code']
	}

class Card(AbstractCard):
	meta = {
		'collection': 'cards',
		'queryset_class': CardQuerySet
	}