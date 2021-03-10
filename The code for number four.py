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
    filtered_list_of_species.to_csv('../filered_list_of_species.csv') # print the filtered list to a csv file in the main directory
    print('The shape of the filtered list of species is as follows')
    print(filtered_list_of_species.shape)

    print('The mean weight of each sex in each month is as follows:-')
    groupby_gender_for_weight = filtered_list_of_species.groupby(['sex','genus'])['weight'].mean() # the combination for the mean weight of each sex in each genus
    print(groupby_gender_for_weight)

main()
    