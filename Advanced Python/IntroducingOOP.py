
#Tạo lớp Hình chữ nhật gồm 2 thuộc tính dai, rong và 2 phương thức dien_tich, chu_vi
class HCN:
    # Khởi tạo phương thức với 2 thuộc tính dai và rong
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
        
    # Tạo phương thức dien_tich 
    def dien_tich(self):
        return self.dai * self.rong

    # Tạo phương thức chu_vi
    def chu_vi(self):
        return 2 * (self.dai + self.rong)

# Tạo đối tượng từ lớp Hình chữ nhât
hcn = HCN(10, 5)

# Gọi phương thức và truy cập thuộc tính của đối tượng
print(f"Các cạnh hình chữ nhật: chiều dài = {hcn.dai}, chiều rộng = {hcn.rong}")
print(f"Diện tích hình chữ nhật: S= {hcn.dien_tich()}")
print(f"Chu vi hình chữ nhật: C = {hcn.chu_vi()}")





