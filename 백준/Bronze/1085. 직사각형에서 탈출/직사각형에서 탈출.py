x, y, w, h = map(int, input().split())
dist = []

dist.append(abs(h - y))
dist.append(abs(w - x))
dist.append(x)
dist.append(y)

print(min(dist))