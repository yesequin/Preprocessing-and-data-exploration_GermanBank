from pandas import DataFrame

def cat_to_num(dataset_input: DataFrame)-> DataFrame:
  '''
  Returns a DataFrame with the next categoric columns converted to numeric columns with values mentioned on each dictionary:
    check_status, credit_history, purpose, savings, present_emp_since, personal_status_sex, other_debtors, property,
     other_installment_plans, housing, job, telephone, foreign_worker.

    Parameters:
      dataset_input: the original DataFrame. Size (1000,21)

    Returns:
      dataset: Another DataFrame with numeric columns only. Size (1000,21) 
  '''
  dataset = dataset_input.copy(deep = True)
  dataset = dataset.drop_duplicates() if dataset.duplicated().any() else dataset #we make sure there is no duplicate data
  dataset = dataset.dropna() if dataset.isnull().values.any() else dataset #we make sure there is no NULL data

  dic_account_check_status = {'no checking account': 4,
                              '< 0 DM': 1,
                              '0 <= ... < 200 DM': 2,
                              '>= 200 DM / salary assignments for at least 1 year': 3
  }
  dic_credit_history = {'existing credits paid back duly till now': 3,
                        'critical account/ other credits existing (not at this bank)': 5,
                        'delay in paying off in the past': 4,
                        'all credits at this bank paid back duly': 2,
                        'no credits taken/ all credits paid back duly': 1
  }
  dic_purpose = {'domestic appliances': 5,
                 'car (new)': 1,
                 'radio/television': 4,
                 'car (used)': 2,
                 'business': 10,
                 '(vacation - does not exist?)': 8,
                 'education': 7,
                 'repairs': 6,
                 'furniture/equipment': 3,
                 'retraining': 9
  }
  dic_savings = {'... < 100 DM': 5,
                 'unknown/ no savings account': 1,
                 '100 <= ... < 500 DM': 4,
                 '500 <= ... < 1000 DM ':3,
                 '.. >= 1000 DM ': 2
  }
  dic_present_emp_since = {'1 <= ... < 4 years': 3,
                        '.. >= 7 years': 1,
                        '4 <= ... < 7 years': 2,
                        '... < 1 year ': 4,
                        'unemployed':5
  }
  dic_personal_status_sex = {'male : single': 3,
                             'female : divorced/separated/married': 2,
                             'male : married/widowed': 4,
                             'male : divorced/separated': 1
  }
  dic_other_debtors = {'none': 1,
                       'guarantor': 3,
                       'co-applicant': 2
  }
  dic_property = {'if not A121/A122 : car or other, not in attribute 6': 3,
                  'real estate': 1,
                  'if not A121 : building society savings agreement/ life insurance': 2,
                  'unknown / no property': 4
  }
  dic_other_installment_plans = {'none': 3,
                              'bank': 1,
                              'stores': 2
  }
  dic_housing = {'own': 2,
                 'rent': 1,
                 'for free': 3
  }
  dic_job = {'skilled employee / official': 3,
             'unskilled - resident': 2,
             'management/ self-employed/ highly qualified employee/ officer': 4,
             'unemployed/ unskilled - non-resident': 1
  }
  dic_telephone ={'none':0,
                  'yes, registered under the customers name ': 1
  }
  dic_foreign_worker = {'yes':1,
                        'no':0
  }
  #we assign the dictionary value to that specific column with .map
  dataset['account_check_status'] = dataset['account_check_status'].map(dic_account_check_status)
  dataset['credit_history'] = dataset['credit_history'].map(dic_credit_history)
  dataset['purpose'] = dataset['purpose'].map(dic_purpose)
  dataset['savings'] = dataset['savings'].map(dic_savings)
  dataset['present_emp_since'] = dataset['present_emp_since'].map(dic_present_emp_since)
  dataset['personal_status_sex'] = dataset['personal_status_sex'].map(dic_personal_status_sex)
  dataset['other_debtors'] = dataset['other_debtors'].map(dic_other_debtors)
  dataset['property'] = dataset['property'].map(dic_property)
  dataset['other_installment_plans'] = dataset['other_installment_plans'].map(dic_other_installment_plans)
  dataset['housing'] = dataset['housing'].map(dic_housing)
  dataset['job'] = dataset['job'].map(dic_job)
  dataset['telephone'] = dataset['telephone'].map(dic_telephone)
  dataset['foreign_worker'] = dataset['foreign_worker'].map(dic_foreign_worker)
  return dataset
