import pandas as pd # this imports pandas like we need to
from pandas import DataFrame

def main():
    species_dataframe = pd.read_csv('species.csv')
    surveys_dataframe = pd.read_csv('surveys.csv')

    left_merge = pd.merge(left=surveys_dataframe,right=species_dataframe, how='left', left_on='species_id', right_on='species_id')
    print('The shape of the inital merged  data frame is:- ')
    print(left_merge.shape) 
    #left_merge.to_csv('../left_merge.csv') if you uncomment this out then you can see if you did the merge right 
    filtered_list_of_species = left_merge[left_merge['genus'].isin(['Dipodomys','Sigmodon','Chaetodipus'])]
    #this will write the genus filtered data frame to a csv file
    filtered_list_of_species.to_csv('../filered_list_of_species.csv')

main()
    