import numpy as np

one_syl = open('single_syl_noun.txt', 'r').read().split()
two_syl = open('two_syl_noun.txt', 'r').read().split()
both = one_syl + two_syl

flip = np.random.randint(4)

title = []

if flip < 3:
    title.append(np.random.choice(one_syl))
    title.append('of')
    title.append(np.random.choice(both))
    title.append('and')
    title.append(np.random.choice(both))
else:
    title.append(np.random.choice(two_syl))
    title.append('of')
    title.append(np.random.choice(one_syl))
    title.append('and')
    title.append(np.random.choice(one_syl))

print ' '.join(title)
