from collections import Counter 
A = 2
B = 9
C = 7
D = 11
E = 35
Mean = (A+B+C+D+E)/5
# print(Mean)

WHJR = "Amazon WhitehatJunior"
data = Counter(WHJR)
# print(data)

new_list = data.items()
print(new_list)

value = data.values()
print(value)