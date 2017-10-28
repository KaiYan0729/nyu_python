#!/usr/bin/env python3

import unittest
from Flatland import Triangle, Square, Circle

class TestTriangle(unittest.TestCase):
	def setUp(self):
		t = Triangle(2)
		self.an_ally = t.add_ally("circle")
		self.an_enemy = t.add_enemy("square")
		self.an_update_edge_length = t.update_edge_length(20)
		self.an_area = t.area
		self.a_perimeter = t.perimeter
		
	def test_add_ally(self):
		self.assertEqual(self.an_ally[0],'circle')
		
	def test_add_enemy(self):
		self.assertEqual(self.an_enemy[0],'square')
	
	def test_updated_edge_lenngth(self):
		self.assertEqual(self.an_update_edge_length,22)		
	
	def test_area(self):
		self.assertEqual(round(self.an_area()), 210)
		
	def test_perimeter(self):
		self.assertEqual(round(self.a_perimeter()), 66)
		
class TestSquare(unittest.TestCase):
	def setUp(self):
		s = Square(2)
		self.an_ally = s.add_ally("circle")
		self.an_enemy = s.add_enemy("triangle")
		self.an_update_edge_length = s.update_edge_length(20)
		self.an_area = s.area
		self.a_perimeter = s.perimeter
		
	def test_add_ally(self):
		self.assertEqual(self.an_ally[0],'circle')
		
	def test_add_enemy(self):
		self.assertEqual(self.an_enemy[0],'triangle')
	
	def test_updated_edge_lenngth(self):
		self.assertEqual(self.an_update_edge_length,22)		
	
	def test_area(self):
		self.assertEqual(round(self.an_area()), 484)
		
	def test_perimeter(self):
		self.assertEqual(round(self.a_perimeter()), 88)
	
class TestCircle(unittest.TestCase):
	def setUp(self):
		c = Circle(2)
		self.an_ally = c.add_ally("triangle")
		self.an_enemy = c.add_enemy("square")
		self.an_update_edge_length = c.update_edge_length(20)
		self.an_area = c.area
		self.a_perimeter = c.perimeter
		
	def test_add_ally(self):
		self.assertEqual(self.an_ally[0],'triangle')
		
	def test_add_enemy(self):
		self.assertEqual(self.an_enemy[0],'square')
	
	def test_updated_edge_lenngth(self):
		self.assertEqual(self.an_update_edge_length,22)		
	
	def test_area(self):
		self.assertEqual(round(self.an_area()), 1521)
		
	def test_perimeter(self):
		self.assertEqual(round(self.a_perimeter()), 138)

if __name__ == '__main__':
	unittest.main()
