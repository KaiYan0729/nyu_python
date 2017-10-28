#!/usr/bin/env python3 
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pandas_datareader.data as web
import datetime    
import scipy.optimize as sco

class Portfolio:
	def __init__(self, ticker, choice):
		#self.shape_type = "triangle"
		self.ticker = ticker
		self.choice = choice
		#self.weights = []
		
		
	def get_data(self):
		#set the staring time and ending time
		start = datetime.datetime(2010, 1, 1)
		end = datetime.datetime(2014, 12, 31)
		#user input equity tickers
		data = pd.DataFrame()
		data[self.ticker] = web.DataReader(self.ticker,'yahoo', start, end)['Adj Close']
		data.colums = self.ticker
		print('\n----------Price Series---------')
		print(data)	
		return data

	def data_analysis(self, weights, data):
		rets = np.log(data / data.shift(-1))
		rf = 0.05 #constant
		weights = np.array(weights)
		annual_ret = np.sum(rets.mean() * weights) * 252
		annual_vol = np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))
		return np.array([annual_ret, annual_vol, (annual_ret - rf) / annual_vol])
'''	
	def objective_function(self, intial_weights, data, choice):
		if choice == 'maximize return':
			func = -t.data_analysis(intial_weights, data)[0]
		elif choice == 'minimize volatility':
			func = t.data_analysis(intial_weights, data)[1]
		elif choice == 'maxmize sharpe ratio':
			func = -t.data_analysis(intial_weights, data)[2]
		return func

	def optimal_weight(self, numTicker, data, choice):
		cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
		bnds = tuple((0, 1) for x in range(numTicker))
		intial_weights = numTicker * [1/ numTicker]
		statistics = sco.minimize(objective_function, intial_weights, args=(data, choice,), method='SLSQP', bounds=bnds, constraints=cons)
		weights = statistics['x'].round(2)
		return weights
	def test(self, final_weight, data, choice):
		output = t.data_analysis(final_weight, data)
		print('If your goal is to {}' .format(choice),', then your portfolio statistics is:\nannualized return = {}'.format(output[0].round(3)), '\nvolatilites = {}'.format(output[1].round(3)), '\nsharpe ratio = {}'.format(output[2].round(3)))

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
'''

def main():
	ticker = ['BK', 'AAPL', 'LUV', 'MCO', 'DVA']
	numTicker = len(ticker)
	choice = 'maximize return'
	t = Portfolio(ticker, choice)
	data = t.get_data()
	#intial_weights = numTicker * [1/ numTicker]
	#a= t.data_analysis(intial_weights, data)
	#print(a)
	#max return
'''
	final_weight = t.optimal_weight(numTicker, data, choice)
	dict_weights = dict(zip(ticker, final_weight))
	print('----------Optimal weights if your goal is to {}'.format(choice), '---------')
	print(dict_weights)
	print('In sample test results--->')
	test_result = t.test(final_weight, data, choice)
	t.portfolio_growth_visualization(data, final_weight, choice)
'''




if __name__ == '__main__':
	main()