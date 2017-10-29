import numpy as np
import pandas as pd
#import matplotlib
import matplotlib.pyplot as plt
import datetime
import pandas_datareader.data as web
import math

import scipy.optimize as sco

#download data from Yahoo Finance and stock growth visuslization
def get_data(ticker):
    # set the staring time and ending time
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime(2014, 12, 31)

    # user input equity tickers
    data = pd.DataFrame()
    data[ticker] = web.DataReader(ticker, 'yahoo', start, end)['Adj Close']
    data.colums = ticker

    #plot stock price over time
    data.plot(figsize=(8, 5))
    plt.title('Stock Price Over Time')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.show()
    #print('\n----------Price Series---------')
    #print(data)
    return data

#Data Analysis to calculate the Return, Risk, and Correlation for each stock
def data_analysis(weights, data):
    rets = np.log(data / data.shift(-1))
    rf = 0.05  # risk free interest rate, constant
    weights = np.array(weights)
    annual_ret = np.sum(rets.mean() * weights) * 252
    annual_vol = np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))
    return np.array([annual_ret, annual_vol, (annual_ret - rf) / annual_vol])

#Define onjection function for portfolio optimization
def objective_function(intial_weights, data, choice):
    if choice == 'Maximize Return':
        func = -data_analysis(intial_weights, data)[0]
    elif choice == 'Minimize Volatility':
        func = data_analysis(intial_weights, data)[1]
    elif choice == 'Maxmize Sharpe Ratio':
        func = -data_analysis(intial_weights, data)[2]
    return func

#calculate optimal weight for each stock
def optimal_weight(numTicker, data, choice):
    cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bnds = tuple((0, 1) for x in range(numTicker))
    intial_weights = numTicker * [1 / numTicker]
    statistics = sco.minimize(objective_function, intial_weights, args=(data, choice,), method='SLSQP', bounds=bnds,
                              constraints=cons)
    weights = statistics['x'].round(2)
    return weights

#statistics for the portfolio
def test(final_weight, data, choice):
    output = data_analysis(final_weight, data)
    print('If your goal is to {}'.format(choice),
          ', then your portfolio statistics is:\nannualized return = {}'.format(output[0].round(3)),
          '\nvolatilites = {}'.format(output[1].round(3)), '\nsharpe ratio = {}'.format(output[2].round(3)))

#portfolio growth visualization
def portfolio_growth_visualization(data, weights, choice):
    rets = np.log(data / data.shift(-1))
    value = rets * weights
    portRet = np.sum(value, axis=1)
    portRet = np.flip(portRet, 0)
    portRet = portRet.cumsum()
    portVal = 10000 * np.exp(portRet) #portfolio value started with $10000 initial investment

    #graph, portfolio growth
    portVal.plot(figsize=(8, 5))
    plt.title('Portfolio Growth Visualization, Type:{}'.format(choice))
    plt.xlabel('Time')
    plt.ylabel('Portfolio Value')

    plt.show()
    return portVal

#portfolio risk visualization(measured by 5% Value-at-Risk(VaR)
def value_at_risk_visualization(data,weights,choice):
    rets = np.log(data / data.shift(-1))
    value = rets * weights
    portRet = np.sum(value, axis=1)
    portRet = np.flip(portRet, 0)
    portRet = portRet.cumsum()
    portVal = 10000 * np.exp(portRet)
    portVal = pd.Series.to_frame(portVal)

    #graph, portfolio returns
    portVal.plot.hist()
    plt.title('Portfolio 5% Value-at-Risk Visualization, Type:{}'.format(choice))
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    #calculate portfolio risk, the 5th percentile(VaR)
    p5 = np.percentile(portVal, 5)
    return p5

def main():
    ticker = ['BK', 'AAPL', 'LUV', 'MCO', 'DVA']
    # user_ticker = input('Please enter the stock ticker you want to include in your portfolio--->')
    # ticker = user_ticker.split(',')
    numTicker = len(ticker)
    data = get_data(ticker)

    # max return
    choice = 'Maximize Return'
    final_weight = optimal_weight(numTicker, data, choice)
    dict_weights = dict(zip(ticker, final_weight))
    print('----------Optimal weights if your goal is to {}'.format(choice), '---------')
    print(dict_weights)
    print('\nIn sample test results--->')
    test_result = test(final_weight, data, choice)
    portfolio_growth_visualization(data, final_weight, choice)
    var5 = value_at_risk_visualization(data,final_weight,choice) #calculate 5% Value at Risk(VaR)
    print('\nThe 5% VaR is --->')
    print(var5)

    # min volatility
    choice = 'Minimize Volatility'
    final_weight = optimal_weight(numTicker, data, choice)
    dict_weights = dict(zip(ticker, final_weight))
    print('----------Optimal weights if your goal is to {}'.format(choice), '---------')
    print(dict_weights)
    print('\nIn sample test results--->')
    test_result = test(final_weight, data, choice)
    portfolio_growth_visualization(data, final_weight, choice)
    var5 = value_at_risk_visualization(data,final_weight,choice) #calculate 5% Value at Risk(VaR)
    print('\nThe 5% VaR is --->')
    print(var5)

    # max sharpe ratio
    choice = 'Maxmize Sharpe Ratio'
    final_weight = optimal_weight(numTicker, data, choice)
    dict_weights = dict(zip(ticker, final_weight))
    print('----------Optimal weights if your goal is to {}'.format(choice), '---------')
    print(dict_weights)
    print('\nIn sample test results--->')
    test_result = test(final_weight, data, choice)
    portfolio_growth_visualization(data, final_weight, choice)
    var5 = value_at_risk_visualization(data,final_weight,choice) #calculate 5% Value at Risk(VaR)
    print('\nThe 5% VaR is --->')
    print(var5)

if __name__ == '__main__':
    main()