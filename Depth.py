from scene import *

class Visual(Scene):
	def setup(self):
		self.background_color = 'white'
		self.rects = []
		
		self.no = 25
		for i in range(self.no):
			col = (1 / self.no) * (self.no - i)
			col = (col, col, col)
			sqr = (self.no - i) * (self.no - i)
			s = ShapeNode(ui.Path.rect(0, 0, self.size.w - (self.no * self.no) + sqr, self.size.h - (self.no * self.no) + sqr), col)
			self.rects.append((s, sqr))
			self.add_child(s)
		
	def update(self):
		g = gravity()
	
		for i in range(self.no):
			items = self.rects[i]
			item = items[0]
			speed = ((items[1] - (self.no * self.no)) * -1)
			item.position = (self.size.w / 2) + (g.y * (speed * -1)), (self.size.h / 2) + (g.x * speed)
		
run(Visual())
