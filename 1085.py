x, y, w, h = list(map(int, input().split()))

x_axis = w-x if (w-x) < x else x
y_axis = h-y if (h-y) < y else y
print(x_axis if x_axis < y_axis else y_axis)