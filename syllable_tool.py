import pronouncing
import re

nounlist = open('singleconv.data.noun', 'r').read()
nounlist = nounlist.split()

single_syl = set()
two_syl = set()
other = set()

for noun in nounlist:
    if not noun[0].isupper():
        phonemes = pronouncing.phones_for_word(noun)
        for phone in phonemes:
            syls = re.sub('\\D', '', phone)
            if len(syls) == 1: 
                single_syl.add(noun)
            if len(syls) == 2: 
                two_syl.add(noun)
            else: 
                other.add(noun)

with open('single_syl_noun.txt', mode='wt') as outfile:
    outfile.write('\n'.join(single_syl))
    outfile.write('\n')

with open('two_syl_noun.txt', mode='wt') as outfile:
    outfile.write('\n'.join(two_syl))
    outfile.write('\n')

with open('longer_noun.txt', mode='wt') as outfile:
    outfile.write('\n'.join(other))
    outfile.write('\n')