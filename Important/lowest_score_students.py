try:
    N = int(input())
except ValueError as va:
    print("expected value is an int")

student_l = []
while True:
    try:
        name = str(input())
    except ValueError as va:
        print ("expected a string input")
        continue

    try:
        score = float(input())
    except ValueError as va:
        print ("expected a int input")
        continue
    student_l.append([name, score])

    if len(student_l) == N:
        break

score_l = []
for score in student_l:
    score_l.append(score[-1])

m = min(score_l)
while m in score_l:
    score_l.pop(score_l.index(m))

new_s = []

for val in student_l:
    if val[-1] == min(score_l):
        new_s.append(val[0])

new_s = sorted(new_s)
for name in new_s:
    print (name)
