def get_height(width, hypo):
    return (hypo ** 2 - width ** 2) ** 0.5

def check(width):
    x_height = get_height(width, x)
    y_height = get_height(width, y)
    return (x_height * y_height) / (x_height + y_height) >= c

x,y,c = map(float,input().split())

start, end = 0, min(x,y)
while end - start >= 10**-4:
    mid = (start+end) / 2

    if check(mid):
        start = mid
    else:
        end = mid

print(f"{start:.3f}")