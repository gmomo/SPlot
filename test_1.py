#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 10:46:05 2017

@author: soumyadipghosh
"""

import quandl 
import matplotlib.pyplot as plt
import pandas as pd

class stock_plotter:
    
    def __init__(self):
        stock_quote = ""
        data = ""
        
    def set_quote(self,s):
        self.stock_quote = s
        self.get_data()
    
    def get_data(self):
        quandl.ApiConfig.api_key = "iFESvvHuEeC_s8RgXxvW";
        self.data = quandl.get("NSE/" + self.stock_quote)
        #print (self.data['Open'])
        
    def stock_plotter(self,s):
        plt.plot(self.data.index,self.data[s])
        plt.xlabel("Year")
        plt.ylabel(s)
        plt.title(self.stock_quote + " Share Price")
        plt.show()
        

s = stock_plotter()
print ("Please set stock ticker");
s.set_quote(input())
print ("Please set column to Print : Open,High,Low,Close,Last")
s.stock_plotter(input())
