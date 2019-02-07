#Import dependencies and file path
import csv
import os
path = os.path.join('.', 'Resources', 'election_data.csv')
output_path = os.path.join('.', 'output', 'output.csv')

#Package variables
votes = 0
candidates = {}
winner = ("Dr. Seuss", 0 )

#Open election data
with open( path, newline='') as csvFile:
    reader = csv.reader( csvFile, delimiter= ',')
    next(reader)

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
for key, value in candidates.items():
    perc = int ((value / votes) * 100000 ) / 1000
    print( f"{key}: {perc}% ({value})" )

#Print winner
print( "__________________________" )
print( f"Winner: {winner[0]}" )
print( "__________________________" )

with open( output_path, 'w', newline='') as csvFile:
    writer = csv.writer( csvFile, delimiter=',')

    writer.writerow( "Election Results" )
    writer.writerow( "________________________" )
    writer.writerow( f"Total Votes: {votes}" )
    writer.writerow( "________________________" )
    
    for key,value in candidates.items():
        perc = int((value / votes) * 100000 ) / 1000
        writer.writerow( f"{key}: {perc}% ({value})" )

    writer.writerow( "________________________" )
    writer.writerow( f"Winner: {winner[0]}" )
    writer.writerow( "________________________" )
