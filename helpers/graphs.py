#libraries needed:
from pandas import DataFrame
from matplotlib.figure import Figure
import matplotlib as plt
import seaborn as sns
import pylab as pl

def hist(dataset:DataFrame)-> Figure:
  '''
  Returns 5 histograms inside a 3x2 subplot with 'genre','marital_status','credit_term_range','age_range','default' column information.

    Parameters:
    dataset: a dataset with only discrete variables.

    Returns:
      Five histograms with information about the columns: 'genre','marital_status','credit_term_range','age_range','default'
  '''
  histogram = ['genre','marital_status','credit_term_range','age_range','default']
  histograms_list = list(enumerate(histogram))
  pl.figure(figsize = (30,20))
  pl.title('Histograms')
  for i in histograms_list:
    pl.subplot(3, 2, i[0]+1) #3 columns, 2 rows
    sns.countplot(x = i[1], data = dataset)
    pl.xlabel(i[1], fontsize=20)
    pl.ylabel('Total', fontsize=20)