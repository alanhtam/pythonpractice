## Challenge 173 from /r/dailyprogrammer: create a unit calculator that 
## converts meters, inches, and attoparsecs. Input must be in the form
## of 'N oldunits to newunits'. Output should be returned as 'N oldunits
## is X newunits'.

conversions = {'inchestoinches': 1,
               'inchestometers': 0.254,
               'inchestoattoparsecs':0.82315794,
               'meterstoinches': 39.3701,
               'meterstometers': 1,
               'meterstoattoparsecs': 32.4077929,
               'attoparsecstoinches': 1.21483369,
               'attoparsecstometers': 0.0308567758,
               'attoparsecstoattoparsecs': 1}

def main(n, oldunit, newunit, conversions):
    print n, oldunit, 'is', n * conversions[oldunit+'to'+newunit], newunit

str = raw_input('Convert what? e.g. 3 inches into meters.').split()
number_input = int(str[0])
old_input = str[1]
new_input = str[3]

main(number_input, old_input, new_input, conversions)