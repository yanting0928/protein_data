comment = """COMPND    MOL_ID: 1;
COMPND   2 MOLECULE: HIV-1 CAPSID PROTEIN;
COMPND   3 CHAIN: A, B, C, D;
COMPND   4 FRAGMENT: C-TERMINAL DOMAIN, UNP RESIDUES 278-363;
COMPND   5 ENGINEERED: YES;
COMPND   6 MUTATION: YES
"""
words = []
lines = comment.splitlines()

for line in lines:
    words.append(line.split()[2:])
print words

mol_id = words[0][0].split(';')[0]
print "mol id is: ", mol_id

molecule = words[1][1:]
print "molecule is: ",molecule


#if chain is not set up in the file,it should be a notice
#two ways for notice

#1
if words[3][0] == "FRAGMENT:":
    fragment = words[3][1:]
    print "fragment is : ",fragment

#2
assert words[3][0] == "FRAGMENT:"