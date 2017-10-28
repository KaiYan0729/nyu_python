#!/usr/bin/env python3

class Shape:
	def __init__(self, edge_length):
		self.edge_length = edge_length

	def update_edge_length(self, change):
		self.edge_length = self.edge_length + change
		return self.edge_length
		
	def add_ally(self,shape_object):
		self.allies.append(shape_object)
		return self.allies
		
	def add_enemy(self,shape_object):
		self.enemies.append(shape_object)
		return self.enemies
		
		
class Triangle(Shape):
	@staticmethod
	def __Calc_area(edge_length):
		return edge_length**2 * 3**0.5 / 4
	
	@staticmethod
	def __Calc_perimeter(edge_length):
		return edge_length * 3
		
	def __init__(self, edge_length):
		super().__init__(edge_length)	
		self.__area = Triangle.__Calc_area(self.edge_length)
		self.__perimeter = Triangle.__Calc_perimeter(self.edge_length)
		self.shape_type = "triangle"
		self.role = "aggressive and prone to violence"
		self.allies = []
		self.enemies = []

class Square(Shape):
	@staticmethod
	def __Calc_area(edge_length):
		return edge_length**2
	
	@staticmethod
	def __Calc_perimeter(edge_length):
		return edge_length * 4
		
	def __init__(self, edge_length):
		super().__init__(edge_length)
		self.__area = Square.__Calc_area(self.edge_length)
		self.__perimeter = Square.__Calc_perimeter(self.edge_length)
		self.shape_type = "square"
		self.role = "complacent and bureaucratic"
		self.allies = []
		self.enemies = []

class Circle(Shape):
	pi = 3.14159
	
	@staticmethod
	def __Calc_area(edge_length):
		return Circle.pi * edge_length * edge_length
	
	@staticmethod
	def __Calc_perimeter(edge_length):
		return 2 * edge_length * Circle.pi
		
	def __init__(self, edge_length):
		super().__init__(edge_length)
		self.__area = Circle.__Calc_area(self.edge_length)
		self.__perimeter = Circle.__Calc_perimeter(self.edge_length)
		self.shape_type = "circle"
		self.role = "Wise and noble"
		self.allies = []
		self.enemies = []


def main():
	t1 = Triangle(3)
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
