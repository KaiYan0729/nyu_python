#!/usr/bin/env python3

from datetime import date
import math
import numpy as np
import sys
from math import *

#Time to expiration in years
t = 1

#Binomial Tree model
def tree(stock_price, strike_price, rf, volatility, div_yield, steps, flavor):
	#Inputs
    Dt = t / steps
    r_Dt = rf * Dt
    exp_r_Dt = math.exp(r_Dt)
    exp_neg_r_Dt = math.exp(-r_Dt)
    exp_div_Dt = math.exp(div_yield * Dt)
    exp_neg_div_Dt = math.exp(-div_yield * Dt)
    sig_sqrt_Dt = volatility * math.sqrt(Dt)
    exp_sig_sqrt_Dt = math.exp(sig_sqrt_Dt)
	
	#probability of step up & down
    u = exp_sig_sqrt_Dt
    d = 1/u
    q = (exp_r_Dt * exp_neg_div_Dt - d) / (u -d)
    p = 1 - q

	#Step by step matrix calculation with estimated price of the underlying 
    sv = np.zeros((steps + 1,steps +1), dtype = np.float64)
    sv[0,0] = stock_price
    z1 = 0 
    for i in range(1,steps + 1, 1):
        z1 = z1 + 1
        for n in range(z1 + 1):
            sv[n,i] = sv[0,0] * (u ** (i - n)) * (d ** n)
			
	#Matrix with the final payoff depending on put or call
    iv = np.zeros((steps + 1,steps +1), dtype = np.float64)
    z2 = 0
    for i in range(1,steps + 1, 1):
        find = False
        for n in range(z2 + 2):
            if flavor == "C":
                iv[n,i] = max(sv[n,i] - strike_price, 0)
            elif flavor == "P":
                iv[n,i] = max(-1 * (sv[n,i] - strike_price), 0)
            else:
                print("fravor has to be 'C' for call and 'P' for put")
                find = True
                break
        if find:
            break
        z2 = z2 + 1
    
	
    pv = np.zeros((steps + 1,steps +1), dtype = np.float64)
    pv[:, steps] = iv[:, steps]
    z3 = steps + 1
    for i in range(steps -1, -1, -1):
        z3 = z3 - 1
        for n in range(z3):
            pv[n,i] = (q * pv[n, i + 1] + p * pv[n + 1, i + 1]) * exp_neg_r_Dt
    return(pv[0,0])

	
#Black-Scholes model
def phi(x):
    #Cumulative distribution function for the standard normal distribution
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

def black_scholes_call(stock_price, strike_price, rf, volatility, div_yield, c_or_p):
	#Black Scholes formula for call and put options
	d1 = (math.log(stock_price/strike_price) + rf - div_yield + volatility**2/2)/volatility
	d2 = d1 - volatility
	#Call price
	call_bs = stock_price * phi(d1) - exp(-rf) * strike_price * phi(d2)
	#Put price
	put_bs = exp(-rf) * strike_price * phi(-d2) - stock_price * phi(-d1)
	if c_or_p == 'C':
		return(call_bs)
	elif c_or_p == 'P':
		return(put_bs)
	else:
		print('You have to select your option to be either a call(C) or a put(P)')
		
if __name__ == "__main__":	
	#inputs for Black Scholes model
	stock_price = float(sys.argv[1])
	strike_price = float(sys.argv[2])
	rf = float(sys.argv[3])
	volatility = float(sys.argv[4])
	div_yield = float(sys.argv[5])
	c_or_p = sys.argv[6]
	
	#inputs for Binomial Tree model
	flavor = c_or_p
	steps = int(sys.argv[7])
	
	#calculate the difference between two methods
	diff = tree(stock_price, strike_price, rf, volatility, div_yield, steps, flavor) - black_scholes_call(stock_price, strike_price, rf, volatility, div_yield, c_or_p)
	print('Price of this option using Binomial Tree model is ', tree(stock_price, strike_price, rf, volatility, div_yield, steps, flavor))  
	print('Price of this option using Black-Scholes model is ', black_scholes_call(stock_price, strike_price, rf, volatility, div_yield, c_or_p))  
	print('Price difference between these two methods is', diff)
	

