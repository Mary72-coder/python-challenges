"""
Solar Cold Room Sizing

PROBLEM
A small cold room for tomatoes will run on solar power.
the farmer must know how many solar panels and batteries to buy
so the cold room keeps running, even through a full day with no sun

WHAT THIS PROGRAM DOES
1. Takes the list of machines in the cold room (watts and hours per day)
2. Works out the energy the cold room uses in one day.
3. Works out how many solar panels are needed.
4. Works out how many batteries are needed for one full day without sun
5. Gives an example cost and checks that plan covers the need.

HOW TO RUN:
 Python solar_cold_room.py

 Note: All the machines, panel, battery and price numbers are examples.
 Change them to match the real equipment and the real quotes you get.

"""

import math # gives us math.ceil, which rounds a number up
# SECTION 1: INPUT DATA (THE FACTS)
# Each machine is a small record card (a dictionary) with three things:
#its name, its power in watts, and how many hours it runs each day

machines =[
    {"name": "Compressor",      "watts": 600, "hours": 8},
    {"name": "Lights",       "watts": 40, "hours": 10},
    {"name": "Fans",       "watts": 100, "hours": 8},
    
    {"name": "Sensors and phone charger",       "watts": 20, "hours": 24},
]

# SOLAR PANEL FACTS
panel_watts = 400 # power of one panel , in watts
sun_hours = 5 # hours per day when the sun is strong enough
system_efficiency = 0.75  # real life loses 25% (cable, dust, heat)
 # the batteries must cover many sunless days

#BATTERY FACTS
battery_volts = 12
battery_amp_hours = 200
usable_fraction = 0.5
days_without_sun = 1


# Examples of prices in Ghana cedis
panel_price = 1500
battery_price = 4000

##SECTION 2: FUNCTIONS (SMALL REUSABLE TOOLS)

def energy_wh(watts, hours):
    """Energy in watt-hours(wh) = power in watts x hours used"""
    return watts*hours


def units_needed(total_needed, per_unit):
    """ How many units to buy. we always round up, because you 
    cannot buy 4.6 panels. If you need 4.6, you must buy 5."""
    return math.ceil(total_needed/ per_unit)

## SECTION 3: ENERGY USED PER DAY
total_wh_per_day = 0
print("ENERGY USED BY EACH MACHINE")
print("------------------")

for machine in machines:
    wh = energy_wh(machine["watts"], machine["hours"])
    total_wh_per_day += wh
    print(machine["name"] , ":" , machine["watts"] , "W x", machine["hours"] , "h =" , wh, "wh")



print()
print("Total energy per day:", total_wh_per_day, "wh")

# SECTION 4: PANELS AND BATTERIES

# Energy that one panel really gives in a day
wh_per_panel = panel_watts * sun_hours * system_efficiency
# number of panels needed
panels = units_needed(total_wh_per_day, wh_per_panel)

#Energy stored in one battery = volts x amp-hours
battery_wh = battery_volts * battery_amp_hours

#ENERGY OF ONE BATTERY THAT WE ALLOW OURSELVES TO USE
usable_battery_wh = battery_wh * usable_fraction
#ENERGY THE BATTERIES MUST HOLD TO COVER THE SUNLESS DAYS
storage_needed_wh = total_wh_per_day * days_without_sun

# NUMBER OF BATTERIES NEEDED
batteries = units_needed(storage_needed_wh, usable_battery_wh)

#SECTION 5: CHECK AND COST
# check: do the panel we chose produce produce enough energy each day?
produced_wh = panels * wh_per_panel
spare_wh = produced_wh - total_wh_per_day

total_cost = panels*panel_price + batteries * battery_price

# SECTION 6: FINAL REPORT
print()
print("SYSTEM SIZE")
print("--------------")
print("one panel gives:" , wh_per_panel, "wh per day")
print("one battery stores:" , battery_wh, "wh (usable:)", usable_battery_wh, "wh)")
print("Batteries needed:", batteries)
print()
print("CHECK")
print("------------")
print("Panels produce:", produced_wh, "wh per day")
print("Spare energy:", spare_wh, "wh per day")
print()
print("EXAMPLES COST")



  
        
