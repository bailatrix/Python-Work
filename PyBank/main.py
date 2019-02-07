#import dependencies
import csv
import os
path = os.path.join( '.', 'Resources', 'budget_data.csv')
output = os.path.join( '.', 'output', 'output.csv')

#Create variables
#To be assigned values later
count = 0
sumPL = 0
maxProfit = ('Octember', 0)
maxLoss = ('Octember', 0)

#Read file
#Parse for values as directed
with open( path, newline='' ) as csvFile:
    reader = csv.reader( csvFile, delimiter = ',' )
    next(reader)

    for row in reader:
        if len(row) > 0:
            outcome = int( row[1] )
            #Increase count and add profit/loss to sum of profits/losses
            count += 1
            sumPL += outcome

            #Check if current profit is greater than current maxProfit
            #If so, swap
            if outcome > maxProfit[1]:
                maxProfit = ( row[0], outcome )

            #Check if current loss is less than current maxLoss
            #If so, swap
            elif outcome < maxLoss[1]:
                maxLoss = ( row[0], outcome )


#Print results to console
print( "Financial Analysis" )
print( "------------------" )
print( f"Total Months: {count}" )
print( f"Total Profit/Loss: ${sumPL}" )
print( f"Average Change: ${sumPL/count}" )
print( f"Greatest Increase in Profits: { maxProfit[0] } ($ { maxProfit[1] })" )
print( f"Greatest Decrease in Profits: { maxLoss[0] } ($ {maxLoss[1] })" )

#Write a file as output
with open( output, 'w', newline='' ) as csvFile:
    writer = csv.writer( csvFile, delimiter = ',')
    writer.writerow( "Financial Analysis" )
    writer.writerow( "------------------" )
    writer.writerow( f"Total Months: {count}" )
    writer.writerow( f"Total Profit/Loss: ${sumPL}" )
    writer.writerow( f"Average Change: ${sumPL/count}" )
    writer.writerow( f"Greatest Increase in Profits: { maxProfit[0]} ($ { maxProfit[1]})" )
    writer.writerow( f"Greatest Decrease in Profits: { maxLoss[0] } ($ {maxLoss[1] })" )
