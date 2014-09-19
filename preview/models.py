from mongoengine import *

# Create your models here.
class Card(Document):
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
	meta = {
		'collection': 'cards',
		'ordering': ['code']
	}