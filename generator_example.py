CORRECT_COMBINATION = (3, 6, 1)

#function to generate sequence
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield(c1, c2, c3)


#Code to find the match
for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBINATION :
        print('Found!')
        break
    print(c1, c2, c3)