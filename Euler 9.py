# Euler 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# first find all permutations of a<b<c where a+b+c=1000
lofa = []
lofb = []
lofc = []
for a in range(0, 997 + 1):
    for b in range(0, 998 + 1):
        for c in range(0, 999 + 1):
            if a < b < c:
                if a + b + c == 1000:
                    if a * a + b * b == c * c:
                        print("answer=", a, b, c)


