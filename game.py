# game of boxing
import boxer

# ask for name
name= raw_input("what's ur name?")
# init boxers
you= boxer.Boxer(name)
rival= boxer.Boxer("enemy")

# game begin
# show info of me and rival
while you.blood>0 or rival.blood>0:
	print you
	print rival

	# show options -> defend or punch
	boxer.options(you, rival)

	# fight!!
	boxer.fight(you, rival)
	# fight until knock down


# show result
boxer.showResult(you, rival)