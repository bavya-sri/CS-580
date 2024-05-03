import random

R1 = [(i, random.randint(1, 5000)) for i in range(1, 101)]
R2 = [(random.randint(1, 5000), j) for j in range(1, 101)]






R1 =[(67, 3198), (7, 3198), (11, 679), (3, 1647), (82, 2537), (51, 4638), (52, 4738), (38, 4721), (39, 2428), (99, 4115)]
R2 = [ (3198, 30), (3198, 100), (2059, 9), (298, 10), (4559, 47), (5, 48), (960, 72), (4709, 73), (1177, 74), (3206, 2)]

def join_relations(R1, R2):
    # Create a hashmap from R2 keyed by attribute B
    hashmap = {}
    for b,c in R2:
        if b in hashmap:
            hashmap[b].append(c)
        else:
            hashmap[b] = [c]
    print("Hashmap of R2 ",hashmap)

    # Perform the join operation
    result = []
    for t in R1:
        if t[len(t) -1] in hashmap:
            for c in hashmap[t[len(t) -1]]:
                t= [i for i in t]
                t.append(c)
                result.append(t)

    return result


joined = join_relations(R1, R2)
print("Join result: ")
for row in joined:
    print(row)




# --------------------------------------------




