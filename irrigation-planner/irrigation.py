#------IRRIGATION PLANNER-----
# PROBLEM
# A tomato farmer needs to know how much water to pump
#from a stream when the rain alone is not enough for her crop

#---- WHAT THIS PROGRAM DOES
# 1. Takes the rainfall(in mm) for each of the last 14 days.
# Works out how much water is still missing each day
#Converts the missing water from millimetres to litres
#Calculates the total water to pump, the pump running time, 
#the petrol needed and petrol cost
# -----LET'S STATRT!!!


# Rainfall in millimetres for each of the 14 days
rain_mm = [0, 2, 0, 8,12, 0, 0, 3, 5, 0, 0, 1, 15, 0]

# water the tomatoes need every day, in mm
need_per_day = 5
# Size of the farm in hectares (1 hectare = 100m X 100m = 10000 square metres)
farm_size_ha = 0.5
#1 mm of water spraed over 1 square metre is exactly 1 litre.
#s 1 mm of water over 1 hectare (10, 000 square metres) is 10, 000 litres.
litres_per_mm_per_ha = 10000
# litres of water needed on THIS farm for every 1 mm of missing water
litres_per_mm_farm = farm_size_ha * litres_per_mm_per_ha

# pump datails (examples values)
pump_litres_per_hour = 600
pump_petrol_per_hour = 1.5
petrol_price = 15

# SECTION 2: DAILY LOOP (work out the missing water for each day)

# this list will store the missing water (in m) for each day
missing_List = []
# counter used to print the day number
day = 0
print("DAILY WATER REPORT")
print("-------------------")
# Go through the rainfall of each day, one at a time
for rain in rain_mm:
    day += 1 # move to the next day number(same as: day = day + 1)
    # Water still needed after the rain has fallen
    missing_mm = need_per_day - rain

    # If it rained MORE than the crop needs, the result is negative.
    # A farmer cannot pump neative water, so we set it to 0.
    if missing_mm < 0:
        missing_mm = 0
        # save today's answer at the end of the list
    missing_List.append(missing_mm)

    #Convert today's missing water from mm to litres for this farm
    litres = missing_mm*litres_per_mm_farm
    print("DAy", day, "-rain:", rain, "mm | pump:", litres, "litres")

    #SECTION3: TOTALS(add everything up)

# Total missing water over the 14 days, in mm
total_mm = sum(missing_List)
#Total water to pump, in liters
total_litres = total_mm * litres_per_mm_farm
# How many hours the pump must run to move that water
pump_hours = total_litres/pump_litres_per_hour

# petrol the pump will burn, in litres
petrol_needed = pump_hours* pump_petrol_per_hour
# Cost of that petrol, in Ghana cedis
petrol_cost = petrol_needed * petrol_price
# Number of days when the rain was enough(nothing to pump).
#A 0 in the list means "no missing water" for that day.
dry_days = missing_List.count(0)

#-----------------SECTION 4: THE FINAL REPORT
print() # empty line to separate the daily report from the summary
print("SUMMARY FOR 14 DAYS")
print("-------")
print("Total missing water", total_mm, "mm")
print("Total litres to pump:" , total_litres)
print("pump hours:", round(pump_hours, 1))
print("petrol needed:", round(petrol_needed, 1), "litres")
print("Petrol cost: GHS" ,round(petrol_cost, 1))
print("Days with no pumping:" , dry_days)