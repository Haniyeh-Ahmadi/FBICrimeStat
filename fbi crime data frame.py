
import pandas as pd
import json

#from PIL.ImageChops import difference

fbiCrimeData = r"D:\dataScienceDAYCHE\season4Python\fbiProject\FBI_CrimeData_2016.json"
# Open and read the JSON file
with open(fbiCrimeData, 'r') as file:
    # Load the file contents into a dictionary
    fbiCrimeData_dict = json.load(file)
# Example: Access the first dictionary in the list
first_item = fbiCrimeData_dict[0]
# Now, you can access keys of the first dictionary
print(first_item.keys())
#print(first_item.values())
# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(fbiCrimeData_dict)
# Display the DataFrame
print(df)
print('#'* 60)
print(df.info())
cols = df.columns
print(cols)
print('#'* 60)

import matplotlib.pyplot as plt
# Convert 'Murder' column to numeric (in case it's stored as strings)
df['Murder'] = pd.to_numeric(df['Murder'])

# Group the data by 'Region' and sum the 'Murder' counts
region_murder_sum = df.groupby('Region')['Murder'].sum().reset_index()

# Display the total murders by region
print(region_murder_sum)
# Define a list of colors for each region (you can assign custom colors)
colors = ['red', 'green', 'blue', 'orange']  # Define custom colors for each region
# Plot the sum of murders by region in a bar chart
plt.bar(region_murder_sum['Region'], region_murder_sum['Murder'], color=colors)

# Add labels and title
plt.xlabel('Region')
plt.ylabel('Total Murders')
plt.title('Total Murders by Region')
# Convert region_murder_sum DataFrame to string for annotation
summary_text = region_murder_sum.to_string(index=False)
# Add an annotation on the plot with the DataFrame summary
plt.annotate(summary_text, xy=(0.1, 0.7), xycoords='axes fraction', fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightyellow'))

# Show the plot
plt.show()

print('#'* 60)

###################################################################
#now I want to merge specific columns
df_merged_data = df.copy()

def convert_to_numeric(df, columns):
    for col in columns:
        df_merged_data[col] = pd.to_numeric(df_merged_data[col])

# List of columns to convert
crime_columns = ['Murder', 'Rape', 'Robbery', 'Assault', 'Burglary', 'Theft', 'Vehicle_Theft']

# Applying the function
convert_to_numeric(df_merged_data, crime_columns)

# Create List of columns
col_list1= ['Murder', 'Rape', 'Robbery', 'Assault']
col_list2= ['Burglary', 'Theft', 'Vehicle_Theft']

# merged column on type of crime
df_merged_data['violent_crimes'] = df_merged_data[col_list1].sum(axis=1)
df_merged_data['Nonviolent_crimes'] = df_merged_data[col_list2].sum(axis=1)

print(df_merged_data)
print('#'* 60)

region_violent_crime_sum = df_merged_data.groupby('Region')['violent_crimes'].sum().reset_index()
print(region_violent_crime_sum)
print('#'* 60)

region_Nonviolent_crimes_sum = df_merged_data.groupby('Region')['Nonviolent_crimes'].sum().reset_index()
print(region_Nonviolent_crimes_sum)
print('#'* 60)

# Define a list of colors for each region (you can assign custom colors)
colors = ['red', 'green', 'blue', 'orange']  # Define custom colors for each region
# Plot the sum of murders by region in a bar chart
plt.bar(region_violent_crime_sum['Region'], region_violent_crime_sum['violent_crimes'], color=colors)

# Add labels and title
plt.xlabel('Region')
plt.ylabel('total_violent_crimes')
plt.title('Total violent_crimes by Region')
# Convert region_murder_sum DataFrame to string for annotation
summary_text = region_violent_crime_sum.to_string(index=False)
# Add an annotation on the plot with the DataFrame summary
plt.annotate(summary_text, xy=(0.1, 0.7), xycoords='axes fraction', fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightyellow'))

# Show the plot
plt.show()

# Define a list of colors for each region (you can assign custom colors)
colors = ['red', 'green', 'blue', 'orange']  # Define custom colors for each region
# Plot the sum of murders by region in a bar chart
plt.bar(region_Nonviolent_crimes_sum['Region'], region_Nonviolent_crimes_sum['Nonviolent_crimes'], color=colors)

# Add labels and title
plt.xlabel('Region')
plt.ylabel('total_Nonviolent_crimes')
plt.title('Total Nonviolent_crimes by Region')
# Convert region_murder_sum DataFrame to string for annotation
summary_text = region_Nonviolent_crimes_sum.to_string(index=False)
# Add an annotation on the plot with the DataFrame summary
plt.annotate(summary_text, xy=(0.1, 0.7), xycoords='axes fraction', fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightyellow'))

# Show the plot
plt.show()
########################################################
# Step 1: Number of unique states
print("number of states:" , df_merged_data['State'].nunique())
# Step 2: Total national violent crimes
NationalSumViolentCrime = df_merged_data['violent_crimes'].sum()
print("total national violent crimes:" , NationalSumViolentCrime)
# Step 3: Calculate national violent crime mean
NationalSumViolentCrimeAverage = (NationalSumViolentCrime/(df_merged_data['State'].nunique()))
print("national violent crimes mean:" ,  NationalSumViolentCrimeAverage)
print('#' * 60)
########################################################


#########################################################
import pandas as pd

# Step 4: Calculate sum of violent crimes by state
state_violentcrimes_sum = df_merged_data.groupby('State')['violent_crimes'].sum().reset_index()
print(state_violentcrimes_sum)
print('#'* 60)

# Step 5: Calculate the difference from the national mean for each state
state_violentcrimes_sum['DifferenceFromMean'] = state_violentcrimes_sum['violent_crimes'] - NationalSumViolentCrimeAverage

# Step 6: Print tabular report
print("Tabular Report: Violent Crimes and Difference from National Mean")
print(state_violentcrimes_sum[['State', 'violent_crimes', 'DifferenceFromMean']])
