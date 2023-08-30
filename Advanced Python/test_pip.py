import matplotlib.pyplot as plt

# Dữ liệu cho biểu đồ
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 8]

# Vẽ biểu đồ đường
plt.plot(x, y, marker='o')

# Đặt nhãn cho trục x và y
plt.xlabel('X Label')
plt.ylabel('Y Label')

# Đặt tiêu đề cho biểu đồ
plt.title('Biểu đồ ví dụ sử dụng matplotlib')

# Hiển thị biểu đồ
plt.show()