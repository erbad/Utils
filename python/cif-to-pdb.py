import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, epilog=" ")
parser.add_argument("-f", dest="file_in", required=True, type=str, help='Input cif file')
parser.add_argument("-o", dest="file_out", required=True, type=str, help='Output pdb file')
args = parser.parse_args()

index, name, atomtype, residue, chain, x, y, z = [], [], [], [], [], [], [], []

PDBstring_format = '{:4}{:2}{:5}{:2}{:3}{:1}{:3}{:1}{:1}{:4}{:4}{:8}{:8}{:8}{:2}{:4}{:2}{:4}\n'


with open(args.file_out, 'w') as fo:
      with open(args.file_in, 'r') as fi:
            for row in fi:
                  cols = row.split()
                  if cols[0] == 'ATOM':
                        fo.write(PDBstring_format.format('ATOM', 
                                                         '', 
                                                         int(cols[1]), 
                                                         '', 
                                                         cols[3].replace('"', ''), 
                                                         '', 
                                                         cols[5], 
                                                         '', 
                                                         cols[6], 
                                                         int(cols[8]), 
                                                         '', 
                                                         float(cols[10]), 
                                                         float(cols[11]), 
                                                         float(cols[12]), 
                                                         '', 
                                                         '1.00', 
                                                         '', 
                                                         '0.00'))
