# Solar Cold Room Sizing

A small Python progarm that works out how many solar panels and batteries a farmer needs to run a cold room.

## THE PROBLEM
crops spoil when they are not kept cool, and many farms have no grid power. A solar cold room can help, but the farmer must know how many panels and batteries to buy. Too few and the cold room stops. Too many and money is wasted.

## WHAT IT DOES
- Takes a list of machines (watts and hours used per day)
-Works out the energy used in one day, in watt-hours
- Works out the number of solar panels needed
- Works out the number of batteries needed to cover a full day without sun
- Checks that the panels make enough energy, and gives an example cost

## How the maths works
- Energy(wh) = watts x hours
-Energy from one panel per day = panel watts x sun hours x efficiency
- Energy stored in one battery (wh) = volts x amp-hours
only half of a battery is used, so it lasts longer
- Numbers of the panel and batteries are always rounded up, because you cannot buy part of a panel

## How to run

You need python 3 installed

## Example output
```
total energy per day: 6880 wh
panels needed: 5
batteries needed: 6
Total: 31500
```
## Limits of this program
All numbers are examples. Use real equipment sizes and real price quotes.
It does not include the extra power a compressor needs when it starts, or losses in an inverter.
- It plans for one day without sun. Several cloudy days in a row need to more batteries

## WHAT I LEARNED
Functions. Lists of dictionaries, rounding up with math.ceil, and turning energy problem into code.