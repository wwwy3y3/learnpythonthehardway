import random

# result
def showResult(boxer1, boxer2):
	if boxer1.blood > boxer2.blood:
		print "you win"
	elif boxer1.blood < boxer2.blood:
		print "you lose"
	else:
		print "no win or lose, fair!"

# options
def options(boxer1, boxer2):
	str= """
	choose one action
	1. punch
	2. defend
	"""
	choice= raw_input(str)

	# action
	if choice == "1":
		boxer1.punch()
	elif choice == "2":
		boxer1.defend()
	else:
		print "unreconized move... so you stay in defend"
		boxer1.defend()

	# rival take action
	rand= bool(random.getrandbits(1))
	if rand:
		# rival punch
		boxer2.punch()
	else:
		# boxer1 defend
		boxer2.defend()



# fight of boxers
def fight(boxer1, boxer2):
	# both defend
	if boxer1.status == boxer2.status == 'defend':
		# nothing happend
		pass
	elif boxer1.status == boxer2.status == 'punch':
		rand= bool(random.getrandbits(1))
		if rand:
			# boxer2 win
			boxer1.hurtBy(boxer2)
		else:
			# boxer1 win
			boxer2.hurtBy(boxer1)
	elif boxer1.status == 'punch' and boxer2.status == 'defend':
		# boxer2 get hurt
		boxer2.defendPunch(boxer1)
	else:
		boxer1.defendPunch(boxer2)


# boxer got his name, blood
class Boxer(object):
	"""
	a boxer
	got his name, blood
	"""
	def __init__(self, name):
		self.name = name
		# init blood, power
		self.blood= 100
		self.power= random.randrange(10, 20)
		self.defendCoef= 0.8
		self.status= None


	def punch(self):
		# possible condition:
		# 1. rival defend -> * 0.8
		# 2. rival attack -> see who get luck
		self.status= 'punch'
		print "%s punch!" % self.name

	def defend(self):
		self.status= 'defend'
		print "%s defend!" % self.name

	def hurtBy(self, boxer):
		self.blood -= boxer.power
		print "%s get hurt %d" % (self.name, boxer.power)


	def defendPunch(self, boxer):
		blood= boxer.power* self.defendCoef
		self.blood -= blood
		print "%s defend a punch, but still get hurt %d" % (self.name, blood)

	def __str__(self):
		string= "name: %s , blood: %d"
		return string % (self.name, self.blood)
		