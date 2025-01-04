import pandas as pd
#read in data
mlbstats = pd.read_csv('Statcast_2019.csv')

#overall pitch usage insight
pitchOvrCounts = mlbstats.pitch_type.value_counts() #get counts of each individual pitch type (output is pandas series with an index for denoted by the pitch type)
total = mlbstats.pitch_type.count() #get total amount of pitches thrown
pitchOvrData = pitchOvrCounts.to_frame() #convert series to dataframe for further analysis
pitchOvrData['pitch_ovr_percentage'] = pitchOvrData['count'] / total #get overall pitch usage percentages for each pitch
print(pitchOvrData)


#individual pitchers and their counts of each pitch thrown
#pitchByPitcher = mlbstats.groupby(['player_name']).pitch_type.value_counts() #for each pitcher, get the usage percentages for all their pitches
#print(pitchByPitcher)
#pitchByPitcher.to_csv('file2.csv') #create a csv file for the data