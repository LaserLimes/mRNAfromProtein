# Set the default number of occurences.
n = 1

# Use the following dictionary to know how many possible RNA seqs could code for each residue.
codon_occurences = {
    'F' : 2,
    'L' : 6,
    'S' : 6,
    'Y' : 2,
    'X' : 3,
    'C' : 2,
    'W' : 1,
    'P' : 4,
    'H' : 2,
    'Q' : 2,
    'R' : 6,
    'V' : 4,
    'A' : 4,
    'D' : 2,
    'E' : 2,
    'G' : 4,
    'M' : 1,
    'N' : 2,
    'I' : 3,
    'T' : 4,
    'K' : 2
}

# The follow loop scans each residue and multiplies it's key value to n.
# n counts the total number of possible RNA sequences. It is a huge number.
with open('rosalind.txt') as f:
    for char in f.readline():
        if char == "\n":
            break
        else:
            n *= codon_occurences[char]

# We multiply by 3 to account for the stop codons which don't appear the in the protein sequence.
# We use modular arithmetic to "shrink" the number to avoid the pitfalls of computing with such large numbers.
print((n * 3) % 1000000)

# The print statement below shows the exact number if you're curious. It's too big to be practical, even for a human reader.
#print(n*3)
