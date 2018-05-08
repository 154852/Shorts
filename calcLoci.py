import re
import math

print('Type the rules for your point, each on a new line, type (n)ext when you are done')
print('''Different Commands:
	equidistant (Point 1 e.g (0,2)) (Point 2) or equi (Point1) (Point2)
	(X) spaces from (Point) (python comparator i.e ==,<=,>=,>,<,!=)
	on line (Line) (in normal form e.g. x=y *Note that 2x will not work, type 2 * x instead)''')

text = input(': ')
commands = []
while not text.startswith('n'):
	commands.append(text)
	text = input(': ')

print('Your commands: ' + str(commands)[1:][:-1])

class Rectangle:
	def __init__(self, x, y, width, height):
		self.x = int(x)
		self.y = int(y)
		self.width = int(width)
		self.height = int(height)

print('Type the size and origin of the grid:')
size = Rectangle(input('x: '), input('y: '), input('width: '), input('height: '))

class Rule:
	def allows(self, point):
		return False
	
class EquiDist(Rule):
	def __init__(self, regex):
		groups = regex.groups(0)
		self.points = []
		
		for i in range(int(len(groups)/2)):
			self.points.append((float(groups[i*2]), float(groups[(i*2)+1])))
		
	def allows(self, point):
		dist = None
		for item in self.points:
			x = abs(point[0] - item[0])
			y = abs(point[1] - item[1])
			dist2 = math.sqrt((x*x) + (y*y))
			if dist == None:
				dist = dist2
			elif dist != dist2:
				return False
		return True
		
class Circle(Rule):
	def __init__(self, regex):
		groups = regex.groups(0)
		self.centre = (float(groups[1]), float(groups[2]))
		self.dist = float(groups[0])
		self.type = groups[3]
	
	def allows(self, point):
		x = abs(point[0] - self.centre[0])
		y = abs(point[1] - self.centre[1])
		dist = math.sqrt((x*x) + (y*y))
		
		return eval(str(dist) + ' ' + self.type + ' ' + str(self.dist))
	
class OnLine(Rule):
	def __init__(self, regex):
		self.line = regex.groups(0)[0].replace('=', '==')#.split('=')
	
	def allows(self, point):
		return eval(self.line.replace('x', str(point[0])).replace('y', str(point[1])))
	
expr = {
	'equidistant PT ?PT': EquiDist,
	'([0-9]+) spaces from PT ([><=! ]+)': Circle,
	'on line LN': OnLine,
	'equi PT ?PT': EquiDist
}
	
parsedCommands = []
point = '\(([0-9\-\.]+), ?([0-9\-\.]+)\)'
line = '([yx]+=[0-9\+\-*/xy]+)'
for cmd in commands:
	found = False
	for rule in expr.keys():
		regex = re.match(rule.replace('PT', point).replace('LN', line), cmd)
		if regex:
			parsedCommands.append(expr[rule](regex))
			found = True
			break
	if not found:
		print('INVALID COMMAND: \'' + cmd + '\'')
			
possible = []
for x in range(size.x, size.x + size.width + 1, 1):
	for y in range(size.y, size.y + size.height + 1, 1):
		point = (x,y)
		valid = True
		for cmd in parsedCommands:
			if not cmd.allows(point):
				valid = False
				break
		if valid:
			possible.append(point)

print()
print('Possiblities: ' + str(possible)[1:][:-1])
