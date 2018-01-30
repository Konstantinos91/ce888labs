#Adds label for x and y axis from https://stackoverflow.com/questions/42223587/plt-scatter-how-to-add-title-and-xlabel-and-ylabel
#Drops Nan values from https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-certain-columns-is-nan

import matplotlib
matplotlib.use('Agg')


import pandas as pd              #manage of the dataset
import random 
import matplotlib.pyplot as plt  #extra customization
import seaborn as sns            #make plots and styles

import numpy as np 
  

# def permutation(statistic, error):


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed()   # It must be faster in order to prevent the use of masked arrays
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	df = df.dropna() 
	print (df.columns)
	#print (df)
	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)   #creates the plot using the data from the file

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	plt.xlabel('Proposed Fleet')  #adds label in x axis
	plt.ylabel('Current Fleet')   #adds label in y axis

	sns_plot.savefig("veh_scaterplot.png",bbox_inches='tight')   #saves scatter plots into png
	sns_plot.savefig("veh_scaterplot.pdf",bbox_inches='tight')   #saves scatter plots into pdf
 
	data = df.values.T[1]
	
	
	print (("Mean: %f")%(np.mean(data)))
	print (("Median: %f")%(np.median(data)))
	print (("Var: %f")%(np.var(data)))
	print (("std: %f")%(np.std(data)))
	print (("MAD: %f")%(mad(data)))

	plt.clf()
	sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('Proposed fleet') 
	axes.set_ylabel('Current fleet')

	sns_plot2.savefig("veh_histogram.png",bbox_inches='tight')
	sns_plot2.savefig("veh_histogram.pdf",bbox_inches='tight')


	
