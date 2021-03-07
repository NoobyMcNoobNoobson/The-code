from datetime import datetime
import pandas as pd
from pandas import DataFrame
import matplotlib as mpl
print ('pandas version: ' + pd.__version__) # this is to make sure that I am using pandas properly
print('matplotlib version: '+ mpl.__version__) # this is to make sure that I am using matplot lib properly

def main():
    data_sample = pd.read_csv('surveys.csv') # this opens the surveys file
    filter_by_year = data_sample[data_sample.year == 1999] # this filers out the years that are 1999
    filer_by_eight = filter_by_year[filter_by_year.weight <= 8] # this filters the year filtered data frame and filter them again by weight 
    print(filer_by_eight.shape) # this is giving me five rows.
    filer_by_eight.to_csv('../Double_filtere.csv') # this makes the required new csv file with the data frame we needed

def test_isin():
    data_sample = pd.read_csv('surveys.csv')
    # surveys_df[surveys_df['species_id'].isin([listGoesHere])] NL DM PF PE DS.
    filtered_list = data_sample[data_sample['species_id'].isin(['NL','DM','PF','DS'])]
    print('The follwoing plots have the given list of species id:-')
    print(filtered_list)

main()
test_isin()

#is this showing up at all
    

