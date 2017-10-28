#!/usr/bin/env python3

class Triangle:
	def __init__(self, edge_length=0):
		self.shape_type = "triangle"
		self.edge_length = edge_length
		self.role = "aggressive and prone to violence"
		self.allies = []
		self.enemies = []
		
		
	def __str__(self):
		to_string = 'shape_type = {}'.format(self.shape_type)
		return to_string

	def area(self):
		return ((3**0.5) / 4) * self.edge_length * self.edge_length
	def perimeter(self):
		return self.edge_length * 3
	def update_edge_length(self, change):
		self.edge_length = self.edge_length + change
		return self.edge_length
	def add_ally(self,shape_object):
		self.allies.append(shape_object)
		return self.allies
	def add_enemy(self,shape_object):
		self.enemies.append(shape_object)
		return self.enemies

class Square:
	def __init__(self, edge_length=0):
		self.shape_type = "square"
		self.edge_length = edge_length
		self.role = "complacent and bureaucratic"
		self.allies = []
		self.enemies = []
		
	def area(self):
		return self.edge_length * self.edge_length
	def perimeter(self):
		return self.edge_length * 4
	def update_edge_length(self, change):
		self.edge_length = self.edge_length + change
		return self.edge_length
	def add_ally(self,shape_object):
		self.allies.append(shape_object)
		return self.allies
	def add_enemy(self,shape_object):
		self.enemies.append(shape_object)
		return self.enemies

class Circle:
	pi = 3.14159
	
	def __init__(self, r=0):
		self.shape_type = "circle"
		self.role = "Wise and noble"
		self.radius = r
		self.allies = []
		self.enemies = []
		
	def area(self):
		return self.__class__.pi * self.radius * self.radius
	def perimeter(self):
		return 2 * self.radius * self.__class__.pi
	def update_edge_length(self, change):
		self.radius = self.radius + change
		return self.radius
	def add_ally(self,shape_object):
		self.allies.append(shape_object)
		return self.allies
	def add_enemy(self,shape_object):
		self.enemies.append(shape_object)
		return self.enemies

def main():
	t1 = Triangle()
	t2 = Triangle(4)
	t1.add_ally("circle")
	t2.add_ally("circle")
	t1.add_enemy("square")
	t2.add_enemy("square")
	print("I am a", t1.shape_type)
	print("My role is", t1.role)
	print("My friends are", t1.allies)
	print("My enemies are", t1.enemies, "\n")
	#print(t1.area(), t1.perimeter())

	s1 = Square(4)
	s2 = Square(4)
	s1.add_enemy("circle")
	s2.add_enemy("circle")
	s1.add_enemy("triangle")
	s2.add_enemy("triangle")
	print("I am a", s1.shape_type)
	print("My role is", s1.role)
	print("My friends are", s1.allies)
	print("My enemies are", s1.enemies, "\n")
	#print(s1.area(), s1.perimeter())
		
	c1 =  Circle(2)
	c2 =  Circle(2)
	c1.add_ally("triangle")
	c2.add_ally("triangle")
	c1.add_enemy("square")
	c2.add_enemy("square")
	print("I am a", c1.shape_type)
	print("My role is", c1.role)
	print("My friends are", c1.allies)
	print("My enemies are", c1.enemies)
	#print(c1.area(), c1.perimeter())

if __name__ == '__main__':
	main()
