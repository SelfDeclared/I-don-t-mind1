#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: Irfan Baharudin
#Group Name: I don't mind
#Class: PN2004Y
#Date: 
#Version:
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
import matplotlib.pyplot as pit
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):
  print("\nThe following dataframe for SEA from 1997 to 2007 are read as follows:")

  #initializing dataframe for SEA region
  SEA = df.iloc[228:360, :9]
  
  #Display all the SEA region from the selected dataframe
  print(SEA)
  
  print('\n######################################')
  print('Period: 1997 - 2007')
  print('Region: South East Asia')
  print('The top 3 countries of total visitors that visited singapore:\n')
  
  #Remove the columns Year and Month on the SEA variable
  NewSEA = SEA.drop(columns=['Year', 'Month'])

  #Converts all values from SEA from object to integer for calculation
  NewSEA[NewSEA.columns] = NewSEA[NewSEA.columns].astype(int)

  #Calculate the total visitors of each countries by summing up the values
  TotalSEA = NewSEA.sum()

  #sort the region to descending order
  SEA = TotalSEA.sort_values(ascending=False)

  #revert the index
  SEA = SEA.reset_index()

  #Add the columns Countries and Visitors to display on the console
  SEA.columns = ['Countries', 'Visitors']

  #Display the top 3 countries in the SEA region with highest visitors
  print(SEA.head(3))

  #Call the display chart function
  displayChart(SEA)
  return

def displayChart(df):
  #Initialise the 2 list Countries and Visitors
  Countries = df['Countries']
  Visitors = df['Visitors']

  figure1,chart = pit.subplots()

  #Visualise the list with a pie chart with the proper properties
  chart.pie(Visitors,
          labels=Countries,
          startangle=100,
          shadow=True,
          explode=(0, 0, 0, 0, 0.4, 0.3, 0.2),
          autopct='%1.1f%%')

  chart.axis('equal')

  #Show legend on the pie chart
  pit.legend()

  #display the pie chart
  pit.show()

  return

#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################