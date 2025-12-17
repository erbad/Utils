import argparse
from numpy import around

# given the number of molecules and the side of the box
# it computes its concentration in micromolar

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, epilog=" ")

parser.add_argument("-nmol", dest="nmol",required=True, type=int, help='number of molecules to insert')
parser.add_argument("-side", dest="side", required=True, type=float, help="side in nm")

args = parser.parse_args()

nmol = args.nmol
side_nm = args.side

n_avo = 6.02214076 * (10**23)

side_dm = side_nm * (10**-8)
conc_molar = nmol / (n_avo * side_dm**3)
conc_micromolar = conc_molar * (10**6)

print(str(around(conc_micromolar, 2)) + ' micromolar')