from random import randint

class Fight(object):

	def __init__(self, hero_life):
		self.hero_life = hero_life
					
	def gothon(self):
		g_shoot = randint (1, 3)
		hits = 0
		print 'Gothon shoots you.'
		if g_shoot == 3:
			self.hero_life -= 1
			print 'The blast hits you'
		
	def blast(self):
		hits = 0
		shoot = randint(1,12)
		gothon_killed = False
		while gothon_killed == False:
			if shoot > 8:
				print "You killed the Gothon with a nice shoot!"
				gothon_killed = True
			elif 4 < shoot < 9 and hits == 0:
				hits += 1
				print "You shoot on Gothon's legs, and it's steel alive."
				f.gothon()
				continue
			elif 4 < shoot < 9 and hits == 1:
				print "You shoots AGAIN on Gothon's army, but it's doesn't resists. It's dead."
				gothon_killed = True
			else:
				print "You totally missed him. Learn to shoot, man!"
				f.gothon()
				
	def run(self):
		escape = randint(1,6)
		if escape > 2:
			print "You run, like a pussy, and escapes from the Gothons."
		else:
			print "You try to run, but the Gothon hits you in the back, you died."
			return 'death'
			
	def enter(self):
		print "You see the Gothon, you try to blast him or you'll run away?"
		choice = raw_input("> ")
		if choice == 'blast':
			f.blast()
		elif choice == 'run':
			f.run()
		elif self.hero_life == 0:
			return 'death'
		else:
			print 'Does not compute'
			f.enter()
		
			
f = Fight(3)
f.enter()
