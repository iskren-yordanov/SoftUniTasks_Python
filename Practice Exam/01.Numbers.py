num = int(input())


def all_combos(num, new_target, target, combo, all):
    if new_target == 0:
        all.append(list(combo))
        #print(combo)
        
    
    if new_target < 0:
        return 

    for n in range(1, new_target+1):

        combo.append(n)
        new_target -= n

        all_combos(n, new_target, target, combo, all)

        new_target += n
        combo.remove(n)

    #return combo

all_combo_list = []

all_combos(1, num, num, [], all_combo_list)

set_shown = set()

#print(all_combo_list)

for l in all_combo_list[::-1]:
    l = sorted(l)
    x = ' + '.join(map(str, l[::-1]))
    if x not in set_shown:
        print(x)
        set_shown.add(x)
    #print(*l, sep = ' + ')