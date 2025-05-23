n = int(input())
best = (0, 0, 0, 0)  # (value, weight, time, quality)

for _ in range(n):
    w, t, q = int(input()), int(input()), int(input())
    value = (w / t) ** q
    if value > best[0]:
        best = (value, w, t, q)

print(f"{best[1]} : {best[2]} = {int(best[0])} ({best[3]})")