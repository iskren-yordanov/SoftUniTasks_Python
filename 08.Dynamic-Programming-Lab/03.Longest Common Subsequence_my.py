# not working .... something is off and I can put my hands on what .....


first = input()
second = input()

found = []

f_cnt = 0
s_cnt = 0

one = True

while True:

 

    if f_cnt == len(first) or s_cnt == len(second):
        break

    if first[f_cnt] == second[s_cnt]:
        found.append(first[f_cnt])
        f_cnt +=1
        s_cnt +=1

        if one == True:
            one = False
        else:
            one = True

        continue

    if f_cnt == len(first):
        one = False

    if s_cnt == len(second):
        one = True

    if one == True:
        f_cnt +=1
    else:
        s_cnt +=1

print(len(found))