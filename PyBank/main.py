#imports
import csv

#path to budget data file
budgetData = '/budget_data.csv'

#Create variables
#To be assigned values later
count = -1
sumPL = 0
avgPL = sumPL / count
maxProfit = ('Octember', 0)
maxLoss = ('Octember', 0)

#Read file
#Parse for values as directed
with open( 'budgetData' ) as csvFile:
    reader = csv.reader( csvFile, delimiter = ',' )

    for row in reader:

        #Ignore first line
        if row[1].type != String:

            #Increase count and add profit/loss to sum of profits/losses
            count += 1
            sumPL += row[1]

            #Check if current profit is greater than current maxProfit
            #If so, swap
            if row[1] > maxProfit[1]:
                maxProfit = ( row[0], row[1] )

            #Check if current loss is less than current maxLoss
            #If so, swap
            elif row[1] < maxLoss[1]:
                maxLoss = ( row[0], row[1] )

#Write a file as output
with open( 'output', mode= 'w' ) as txtFile:
    writer = csv.writer( txtFile, delimiter = ',')

    writer.writerow( "Financial Analysis" )
    writer.writerow( "------------------" )
    writer.writerow( f"Total Months: {count}" )
    writer.writerow( f"Total Profit/Loss: ${sumPL}" )
    writer.writerow( f"Average Change: ${avgPL}" )
    writer.writerow( f"Greatest Increase in Profits: { maxProfit(0) } ($ { maxProfit(1)})" )
    writer.writerow( f"Greatest Decrease in Profits: { maxLoss(0) } ($ {maxLoss(1) }" )


#Print results to console
print( "Financial Analysis" )
print( "------------------" )
print( f"Total Months: {count}" )
print( f"Total Profit/Loss: ${sumPL}" )
print( f"Average Change: ${avgPL}" )
print( f"Greatest Increase in Profits: { maxProfit(0) } ($ { maxProfit(1) })" )
print( f"Greatest Decrease in Profits: { maxLoss(0) } ($ {maxLoss(1) }" )
