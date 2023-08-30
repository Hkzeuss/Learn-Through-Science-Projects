class NguoiDung:
    def __init__(self, ten, sdt, email):
        self.ten = ten
        self.sdt = sdt
        self.email = email
    
    def hien_thi_thong_tin(self):
        print(f"Tên: {self.ten}")
        print(f"Số điện thoại: {self.sdt}")
        print(f"Email: {self.email}")
        
# Tạo đối tượng từ lớp NguoiDung
nguoi1 = NguoiDung("Chu Tuan V", "123456789", "a@example.com")
nguoi2 = NguoiDung("Pham Quoc H", "987654321", "b@example.com")

# Gọi phương thức hiển thị thông tin
nguoi1.hien_thi_thong_tin()
print("------------")
nguoi2.hien_thi_thong_tin()
