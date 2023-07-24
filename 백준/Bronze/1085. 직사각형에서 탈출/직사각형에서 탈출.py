x, y, w, h = map(int, input().split())

ld = x
xd = y
wd = w - x
hd = h - y

lit = [ld, xd, wd, hd]

print(min(lit))