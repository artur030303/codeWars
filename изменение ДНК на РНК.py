def dna_to_rna(dna):
    new_string = ''
    for word in dna:
        if word == 'T':
            new_string += 'U'
        else:
            new_string += word
    return new_string


print(dna_to_rna('GATTACA'))
