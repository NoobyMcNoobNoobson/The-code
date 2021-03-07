import pandas as pd # this imports pandas like we need to
from pandas import DataFrame

def main():
    species_dataframe = pd.read_csv('species.csv')
    surveys_dataframe = pd.read_csv('surveys.csv')

    left_merge = pd.merge(left=surveys_dataframe,right=species_dataframe, how='left', left_on='species_id', right_on='species_id')
    print(left_merge.shape)

main()
    