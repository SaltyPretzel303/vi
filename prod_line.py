#!/usr/bin/python

l1 = [7, 9, 3, 4, 8, 4]
cf1 = [2, 3, 1, 3, 4, 3]

l2 = [8, 5, 6, 4, 5, 7]
cf2 = [2, 1, 2, 2, 1, 2]

dir1 = []
dir2 = []

cost1 = []
cost2 = []

upper = 2 + l1[0]
lower = 4 + l2[0]
cost1.append(upper)
cost2.append(lower)

for step in range(1, len(l1)):
    upper = cost1[step-1]
    lower = cost2[step-1]

    if upper < lower + cf2[step-1]:
        print(f"{upper} + {l1[step]} = {upper + l1[step]}")
        cost1.append(upper + l1[step])
        dir1.append(1)
    else:
        print(
            f"{lower} + {cf2[step-1]} + {l1[step]} = {lower + cf2[step-1]+l1[step]}")
        cost1.append(lower + cf2[step-1] + l1[step])
        dir1.append(2)

    if lower < upper + cf1[step-1]:
        print(f"{lower} + {l1[step]} = {lower + l2[step]}")
        cost2.append(lower + l2[step])
        dir2.append(2)
    else:
        print(
            f"{upper} + {cf1[step-1]} + {l2[step]} = {upper + cf1[step-1] + l2[step]}")
        cost2.append(upper + cf1[step-1] + l2[step])
        dir2.append(1)

    # upper = min(stat_1+f1(i), stat_2+cf2[i-1]+f2(i))
    # lower = min(lower+f2(i), upper+cf1[i-1]+f2(i))

    # cost1.append(upper)
    # cost2.append(lower)

    print()


print(cost1)
print(cost2)

print(dir1)
print(dir2)
