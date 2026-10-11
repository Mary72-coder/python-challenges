# Post-Harvest Loss tracker
A small python program that finds which crops lose the most to spoilage at a market.

## The problem
Many crops spoil before they reach buyers, and farmers lose money. A market needs to know which crops lose the most, so it can decide where to improve storage, packing or transport.

## What it does
- Reads delivery records (crop, kg delivered, kg spoiled) from a csv file

- adds up the totals for each crop
-Works out the loss percentage for each crop
- Ranks the crops from the worst loss to the best
- Prints the overall loss for the whole market

## How the maths works
Loss percentage = spoiled kg/ delivered kg x 100

the totals for each crop are added up first, and then the percentage of each deliveru, because a large delivery should count more than a small one.
## How to run
You need python 3 installed. keep `deliveries.csv` in the same folder as `loss-tracker.py`. then , in a terminal

python loss_tracker.py

##Example output
CROPS RANKED FROM THE WORST TO BEST

tomato: 15.33% lost | 69 kg of 450 kg 
cassava : 6.91% lost | 38 kg of 550 kg
maize : 4.56% lost | 41 kg of 900 kg

WHOLE MARKET
Total delivered: 1900 kg
Total spoiled: 148 kg
Overall loss: 7.79%

## use your own dat
Replace the line in `deliveries.csv` with real deliveries. keep the first line ( the headings) and use the same colums.

## WHAT I LEARNED
Reading files, dictionaries, string methods, sorting and turning a real post-harvest problem into code