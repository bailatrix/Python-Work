#Import dependencies and file path
import csv
import os
path = os.path.join('.', 'Resources', 'election_data.csv')

#Package variables
votes = 0
candidates = {}
winner = ("Dr. Seuss", 1000000 )

#Open election data
with open( path, newline='') as csvFile:
    reader = csv.reader( csvFile, delimiter= ',')

    #Loop through all rows of data in file
    #Increase total vote count
    for row in reader:
        votes += 1

        #Check if current candidate has been voted for
        #If they are, increase their vote count
        if row[2] in candidates:
            candidates[ row[2] ] += 1

            #Check if there is a new winner
            if candidates[ row[2] ] > winner[1]:
                winner = ( row[2], candidates[ row[2] ] )
        
        #Add candidate to dict if they have not been voted for
        else:
            candidates[ row[2] ] = 1

#Print Voting Result output to console
print( "Election Results" )
print( "__________________________" )
print( f"Total Votes: {votes}" )
print( "__________________________" )

#Printing all candidates, respective percent of votes, count of votes
for key, value in candidates.iteritems():
    perc = int ((value / votes) * 10000 ) / 1000
    print( f"{key}: {perc}% ({value})" )

#Print winner
print( "__________________________" )
print( f"Winner: {Winner}" )
print( "__________________________" )
