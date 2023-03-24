#using hw 4 as a framework
import pandas as pd

file_name = "/Users/mariamabah/Downloads/NU bird strikes 2017 to 2021.xlsx"

collision_data = pd.read_excel(file_name)
print(collision_data)

#get the building with the most longged collisions, make separate table
collisions_by_building = pd.DataFrame(collision_data.get(["Building"]).value_counts())
print(collisions_by_building)
#collisions_by_building = collisions_by_building.rename(columns={" ":"No. of Collisions"})

filename1 = "collisions_by_building.csv"
collisions_by_building.to_csv(filename1)
#bar graph


#get the species with the most logged collisions, make separate table
collisions_by_species = pd.DataFrame(collision_data.get(["Species Name"]).value_counts())

print(collisions_by_species)
filename2 = "collisions_by_species.csv"
collisions_by_species.to_csv(filename2)
#bar graph

#collisions by date
collisions_by_date = pd.DataFrame(collision_data.get(["Date", "Time"]).value_counts())
print(collisions_by_date)

filename3 = "collisions_by_date.csv"
collisions_by_date.to_csv(filename3)
#do a time series plot for this one to show when collisions are more likely

#^^make plots of the above 

#2.24.23
#tried to rename collums of value counts data, but it didn't work

#times series for KGH

timeseries = pd.DataFrame(collision_data.get(["Date", "Building"]))
print(timeseries)

timeseries.drop(timeseries[timeseries["Building"]== "?"].index, inplace=True)
timeseries.drop(timeseries.index[2462:2470], inplace=True)
print(timeseries)


filename4 = "time_series.csv"
timeseries.to_csv(filename4)