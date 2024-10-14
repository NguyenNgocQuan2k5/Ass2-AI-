#A
import numpy as np
foo = np.arange(30)
print("foo:\n", foo)
print("Shape of foo:", foo.shape)

#B
bar = foo.reshape(5, 6)
print("\nbar:\n", bar)
print("Shape of bar:", bar.shape)

#C
baz = foo.reshape(2, 3, 5)
print("\nbaz:\n", baz)
print("Shape of baz:", baz.shape)

#D
bar[1, 0] = -1
print("\nModified bar:\n", bar)
print("\nfoo after modifying bar:\n", foo)
print("baz after modifying bar:\n", baz)

#E
sum_axis_1 = np.sum(baz, axis=1)
print("\nSum of baz over axis 1:\n", sum_axis_1)
sum_axis_2 = np.sum(baz, axis=2)
print("\nSum of baz over axis 2:\n", sum_axis_2)
sum_axis_0_2 = np.sum(baz, axis=(0, 2))
print("\nSum of baz over axes 0 and 2:\n", sum_axis_0_2)

#F
second_row = bar[1, :]
print("\nSecond row of bar:\n", second_row)
last_column = bar[:, -1]
print("\nLast column of bar:\n", last_column)
top_right_2x2 = bar[:2, -2:]
print("\nTop right 2x2 submatrix of bar:\n", top_right_2x2)