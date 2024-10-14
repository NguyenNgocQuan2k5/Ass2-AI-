#A
import numpy as np
vector = np.arange(10) + 1
print("Vector 1 đến 10:\n", vector)

#B
A = vector.reshape(10, 1) + vector
print("\nMa trận 10x10 A:\n", A)

#C
import numpy.random as npr
data = np.exp(npr.randn(50, 5))
print("\nDữ liệu giả lập (50x5):\n", data)
 
#D
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
print("\nTrung bình của từng cột:\n", mean)
print("\nĐộ lệch chuẩn của từng cột:\n", std)

#E
normalized = (data - mean) / std
normalized_mean = np.mean(normalized, axis=0)
normalized_std = np.std(normalized, axis=0)
print("\nTrung bình của các cột đã chuẩn hóa:\n", normalized_mean)
print("\nĐộ lệch chuẩn của các cột đã chuẩn hóa:\n", normalized_std)