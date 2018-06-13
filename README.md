# Dyscalculia_Change_Making

This is a fast prototype for Change Making App for Dyscalculia. The objective of the App is to make it easier for dyscalculia to handle cash. This repo is only for algorithm part of the design. The future plan includes integrating user interface (in a matter that's easy for dyscalculia to use) and this algorithm into a phone App.

## How to Run?

Download and run Test.py.
The class dyscal() is in change_making.py

## Things to do

- Regulate the return message from dyscal.ChangeMaking()
	For the purpose of testing it by another python script that goes over all cases from $0.00 to $200.00 by each step of $0.01. By analyzing the statistic distribution on time, we can make the claim of the algorithm's speed.

- Consider different chang-making options
	Currently, the algorithm tries to accomplish the bill as less item as possible. But consider a case that the bill is $3, wouldn't it be better if you receive a $5 *bill* change if you pay $8 somehow. That indicates different preferences of the algorithm:
	- Least item give
	- Least item receive
	- Least coin receive
	- Greatest decrease in the amount of item on the wallet
	- Save some coins for future convenience
	- etc...

	Also, these would affect what the process should be. （Do users pick one every time? Or leave the preference in the setting? Or have a small test so somehow know their preference? Or dynamically change the algorithm based on the current condition of wallet?)
