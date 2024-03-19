#Libraries needed:
from pandas import DataFrame
import pandas as pd

def continue_to_discrete(dataset_input:DataFrame)-> DataFrame:
  '''
  Returns a new DataFrame with the next modifications:
   - Modifying column 'genre' and 'marital_status' to range values (0 and 1).
   - Creating new columns 'age_range', 'credit_term_range', 'credit_amount_range', 'credit_term_range' with discrete values . 
   - Dropping columns 'personal_status_sex','age', 'duration_in_month','credit_amount', already replaced with the new columns.

   Parameters:
      dataset_input: the DataFrame with int64 DataType . Size (1000,21)

    Returns:
      dataset: Another DataFrame with discrete values. Size (1000,22) 
  '''
  dataset = dataset_input.copy(deep = True)
  dic_genre = {2:1, 1:0, 3:0, 4:0}
  dic_marital_status = {3:1, 5:1, 1:0, 2:0, 4:0}
  dataset['genre'] = dataset['personal_status_sex'].map(dic_genre)
  dataset['marital_status'] = dataset['personal_status_sex'].map(dic_marital_status)
  dataset['age_range'] = pd.cut(x=dataset['age'], #cutting the data into ranges
                                bins=[18, 30, 40, 50, 60, 70, 80], #this will be the range values
                                labels = [1, 2, 3, 4, 5, 6]).astype(int) #this will be the new values: an age from 18 to 30 will be 1, 31 to 40 will be 2...
  dataset['credit_term_range'] = pd.cut(x=dataset['duration_in_month'],
                                        bins=[1, 12, 24, 36, 48, 60, 72],
                                        labels = [1, 2, 3, 4, 5, 6]).astype(int)
  dataset['credit_amount_range'] = pd.cut(x=dataset['credit_amount'],
                                          bins=[1, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000,
                                                14000, 15000, 16000, 17000, 18000, 19000, 20000],
                                          labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]).astype(int)
  dataset['credit_term_range'] = pd.cut(x=dataset['duration_in_month'],
                                        bins=[1, 12, 24, 36, 48, 60, 72],
                                        labels = [1, 2, 3, 4, 5, 6]).astype(int)

  dataset = dataset.drop(columns=['personal_status_sex','age', 'duration_in_month','credit_amount']) #deleting the replaced columns
  return dataset
