import pandas as pd # this imports pandas like we need to
from pandas import DataFrame # this will import dataframe from pandas as we need it
from pandas.core.groupby.groupby import GroupBy # I have no idea why visual studio code automatically inserted this here.
import matplotlib.pyplot as plt # in case we need it
print ('pandas version: ' + pd.__version__) # I am using this to make sure I am in the right environment

import os # to collect the files from the corresponding diretory 
from os import path # taking the right module from the library

def main(): # this connects all the other functions togethe
    the_size()
    mean_hindfoot_lenght()
    mean_plot()
    mean_weight_by_sex_in_each_month()
    males_females_missing_data()


def the_size(): # this will print the shape of the csv file.
    data_sample = pd.read_csv("surveys.csv") # dear paul, this code is designed to have the csv files in the corresponding directory, this should not be a problem since you will get the github link with the csv files as needed 
    print('The shape of the surveys csv files is listed as follows :- ') 
    print(data_sample.shape) # this will give use the shapes

def mean_hindfoot_lenght(): # this is the function that will give us mean hind foot length
    data_sample = pd.read_csv('surveys.csv') # open the file as needed 
    print('The hindfoot lenght for the males and the females are as follows')# this is just to make the printout look a bit more natural 
    groupby_sex = data_sample.groupby(['sex'])['hindfoot_length'].mean() # for some reason this print the data type as well, right now no idea why 
    print(groupby_sex)

def mean_plot():
    data_sample = pd.read_csv('surveys.csv') # open the file as needed 
    print('The mean weight by plot for is as follows:-') # this is just to make the printout look a bit more natural
    groupby_plot = data_sample.groupby(['plot_id'])['weight'].mean() # this one filters the plod_id and then gives us the mean
    print(groupby_plot)

def mean_weight_by_sex_in_each_month(): # the function for mean weight of the sexes in each month
    data_sample = pd.read_csv('surveys.csv')
    print('The mean weight of each sec in each month is as follows:-')
    groupby_month = data_sample.groupby(['sex','month'])['weight'].mean() # filter by sex and month and then give the mean
    print(groupby_month)

    month_dataframe = data_sample.groupby(['month','sex']) # this is the one that makes the plot
    By_month_and_weight = month_dataframe['weight'].mean() # to make the final data frame for the plot

    By_month_and_weight.plot.bar(colormap = 'pink', xlabel = 'Month and sex', ylabel ='Mass (g)', title = 'Mean weight of males and females by month')
    
    print(By_month_and_weight.plot) # this prints the plot

def males_females_missing_data():
    data_sample = pd.read_csv('surveys.csv')
    counts_by_sex = data_sample['sex'].value_counts() # filter by gender
    count_by_null = data_sample['sex'].isna().sum() # filter out the NaN
    print('The number of males and females is:')
    print(counts_by_sex) # print the data frame with the counts by sex 
    print('The number of null values is: ')
    print(count_by_null) # print the data frames that count by null

main()
    
    
