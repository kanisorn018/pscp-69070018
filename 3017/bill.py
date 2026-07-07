"""bill"""
x = int(input())
s = x*0.1
if s < 50:
    s = 50
if s > 1000:
    s = 1000
v = (x+s)*0.07
print(f"{x+s+v:.2f}")
