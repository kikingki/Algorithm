h = []
b = []

for _ in range(3):
    h.append(int(input()))
for _ in range(2):
    b.append(int(input()))
    
print(min(h)+min(b)-50)