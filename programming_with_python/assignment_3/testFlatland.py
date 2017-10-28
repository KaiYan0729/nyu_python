#!/usr/bin/env python3

import unittest
from Flatland import Triangle

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
		self.assertEqual(self.an_area(), 209.57814771583415)
		
	def test_perimeter(self):
		self.assertEqual(self.a_perimeter(), 66)
		
if __name__ == '__main__':
	unittest.main()
