class SinhVien:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    
    def gioi_thieu(self):
        print(f"Xin chào, tôi là {self.ten} và tôi {self.tuoi} tuổi.")

# Tạo đối tượng từ lớp SinhVien
sv = SinhVien("Chu Tuan Viet", 20)

# Gọi phương thức của đối tượng
sv.gioi_thieu()
