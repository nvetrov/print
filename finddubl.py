from collections import Counter

with open('Printers.csv', 'r') as file:
    ff = file.read().split()
dict_printer = {'User': []}
for i in range(len(ff) - 1):
    if ff[i].startswith('S'):
        dict_printer['User'].append(ff[i].split('|')[0])
counter = Counter(dict_printer['User'])
for computer in counter:
    if counter[computer] > 1:
         print(computer)
    else:
        continue
print('Done')
