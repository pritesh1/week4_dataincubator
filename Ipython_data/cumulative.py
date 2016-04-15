import numpy as np
import pandas as pd
class Cumulative:
	def __init__(self):
		self.data=pd.DataFrame()

	def calculate_random(self,input,a,j,f,option='random walk'):
		A=[100,102.9,99.7,94.8,96.2,103.2,111.3,109.2,104.3]
		return A	


	def calculate_rebalancer(self,input,a,j,f,option='random walk'):
		A=[100,101.2,99.7,99.2,100.1,98.2,106.9,104.2,102.3]
		return A


	def calculate_prediction(self,input,a,j,f,option='random walk'):
		A=[100,102.9,101.7,103.4,99.9,105.2,112.3,115.2,109.9]
		return A