notebook = []
while True:
    a = input()
    if a == 'q':
        break
    a = int(a)
    notebook.append(a)

sum = 0
for a in notebook:
    sum = sum + a
j = len(notebook)
ave = sum/j
print(ave)
b = 1
for c in notebook:
    b = b*c
print(b)       