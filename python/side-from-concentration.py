from numpy import around
import argparse

# python side-from-concentration.py -nmol n -conc c 

# given number of molecule and the concentration in micromolar
# it computes the side of the cubic box to use in simulations

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, epilog=" ")

parser.add_argument("-nmol", dest="nmol",required=True, type=int, help='number of molecules to insert')
parser.add_argument("-conc", dest="conc", required=True, type=float, help="concentration in micromolar")

args = parser.parse_args()

nmol = args.nmol
conc = args.conc

n_avo = 6.02214076 * (10**23)
con_molar = conc * (10**-6)
den = n_avo * con_molar

side = (nmol / den) ** (1/3)

side_nm = side * (10**8)

print('Side is %snm' %(around(side_nm, 2)))
