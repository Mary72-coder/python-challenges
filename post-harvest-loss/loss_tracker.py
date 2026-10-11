#POST-HARVEST LOSS TRACKER
#PROBLEM:
# many crops spoil before they reach buyers, and farmers lose money.
# a market needs to know which crop lose the most.
# WHAT THIS PROGRAM DOES:
## reads delivery records from a csv file (delivery.cvs).
##2 Adds up the kg delivered and the kg spoiled for each crop.
##3 Works out the loss percentage for each crop
##4 Ranks the crops from the worst loss to the best.
##5 Prints the overall loss for the whole market.

# HOW TO RUN
# python loss_tracker.py
# (deliveries.cvs must be in the same folder as htis file)


# SECTION 1: READ THE FILE AND ADD UP EACH CROP

# Two dictionaries (record books). the crop name is the label

delivered = {} # crop -> total kg delivered
spoiled = {} # crop -> total kg spoiled

# open the file. "with" closes it for us when we are finished.
with open("deliveries.csv") as file:
    next(file) # skip the line, because it only holds the headings

    for line in file:
        line = line.strip() # remove the invisible new-line mark at the end
        #Skip any empty line
        if line == "":
            continue
    # Cut the line at each comma, e.g. "tomato,200,30"->three pieces
        crop, delivered_kg, spoiled_kg = line.split(",")
    # Everything read from a file is text, so turn the numbers into real numbers
    delivered_kg = int(delivered_kg)
    spoiled_kg = int(spoiled_kg)

    # If we have seen this crop before, add to its totals.
    # If not, start its totals for the first time.
    if crop in delivered:
        delivered[crop] += delivered_kg
        spoiled[crop] += spoiled_kg
    else: 
        delivered[crop] = delivered_kg
        spoiled[crop] = spoiled_kg

#SECTION 2: WORK OUT JTHE LOSS PERCENTAGE FOR EACH CROP

loss_percent = {} #crop -> percentage lost

for crop in delivered:
    #loss % = spoiled/delivered*100
    loss_percent[crop] = spoiled[crop]/delivered[crop]*100

# put the crop names in order, biggest loss first.
# key=loss_percent.get means "order the crops by their loss percentage".
ranked = sorted(loss_percent, key=loss_percent.get, reverse=True)

#---SECTION 3: REPORT

print("CROPS RANKED FROM WORST TO BESTs")
print("------------------")
for crop in ranked:
    print(crop, ":", round(loss_percent[crop],2), "% lost |",
          spoiled[crop], "kg of" , delivered[crop] , "kg")

    # Overall loss for the whole market
total_delivered = sum(delivered.values())
total_spoiled = sum(spoiled.values())
overall_loss = total_spoiled/total_delivered*100

print()
print("WHOLE MARKET")
print("-----------------")
print("Total delivered:" , total_delivered, "kg" )
print("Total spoiled:" , total_spoiled, "kg")
print("Overall loss:" , round(overall_loss, 2) , "%")