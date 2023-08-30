class Tai_lieu():
    def __init__ (self, ma, so_luong):
        self.ma = ma
        self.so_luong = so_luong

class Sach(Tai_lieu):
    def __init__ (self, ma = '',so_luong = '', so_trang = ''):
        super().__init__ (ma, so_luong)
        self.so_trang = so_trang
            
class Tap_chi(Tai_lieu):
    def __init__ (self, ma = '',so_luong = '', thang_ph = ''):
        super().__init__ (ma, so_luong)
        self.thang_ph = thang_ph
            
class Bao(Tai_lieu):
    def __init__ (self, ma = '',so_luong = '', ngay_ph = ''):
        super().__init__ (ma, so_luong)
        self.ngay_ph = ngay_ph

sach = Sach(883, 2003, 88)
tap_chi = Tap_chi(808, 3203, 8)
bao = Bao(888, 8823, 23)
print(f"Sách: \nMã số: {sach.ma} \nSố lương:{sach.so_luong} \nSố trang: {sach.so_trang}")
print(f"\nTạp chí: \nMã số: {tap_chi.ma} \nSố lương:{tap_chi.so_luong} \nTháng phát hành: {tap_chi.thang_ph}")
print(f"\nBáo: \nMã số: {bao.ma} \nSố lương:{bao.so_luong} \nNgày phát hành: {bao.ngay_ph}")
