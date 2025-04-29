import pandas as pd

class Info_Xe:
    def __init__(self, loai_xe, chu_xe, thoi_gian, bien_so_xe=None):
        self.loai_xe = loai_xe
        self.chu_xe = chu_xe
        self.thoi_gian = thoi_gian 
        self.bien_so_xe = bien_so_xe

    def __str__(self):
        return f"Loại xe: {self.loai_xe}, Chủ xe: {self.chu_xe}, Thời gian gửi xe: {self.thoi_gian} giờ, Biển số: {self.bien_so_xe if self.bien_so_xe else 'Không có'}"

class Money_Time:
    def __init__(self):
        self.gia_xe = {
            "Xe đạp": 2,
            "Xe máy": 5,
            "Xe điện": 3.5,
            "Ô tô": 10
        }
    
    def tinh_gia(self, loai_xe, thoi_gian):
        if loai_xe in self.gia_xe:
            return self.gia_xe[loai_xe] * thoi_gian
        return 0  
    
class QuanLyXe:
    def __init__(self):
        self.danh_sach_xe = []
        self.money_time = Money_Time()

    def them_xe(self, xe):
        self.danh_sach_xe.append(xe)
    
    def sua_xe(self, bien_so_xe, loai_xe=None, chu_xe=None, thoi_gian=None):
        for xe in self.danh_sach_xe:
            if xe.bien_so_xe == bien_so_xe:
                if loai_xe: xe.loai_xe = loai_xe
                if chu_xe: xe.chu_xe = chu_xe
                if thoi_gian: xe.thoi_gian = thoi_gian
                break

    def xoa_xe(self, bien_so_xe):
        self.danh_sach_xe = [xe for xe in self.danh_sach_xe if xe.bien_so_xe != bien_so_xe]

    def tinh_gia_xe(self):
        for xe in self.danh_sach_xe:
            xe.gia_gui = self.money_time.tinh_gia(xe.loai_xe, xe.thoi_gian)
    
    def xuat_thong_tin_xe_tren_20k(self):
        xe_tren_20k = [xe for xe in self.danh_sach_xe if xe.gia_gui > 20]
        return xe_tren_20k
    
    def ghi_du_lieu_vao_excel(self, filename="data_xe.xlsx"):
        data = []
        for xe in self.danh_sach_xe:
            data.append([xe.loai_xe, xe.chu_xe, xe.thoi_gian, xe.bien_so_xe, xe.gia_gui])
        df = pd.DataFrame(data, columns=["Loại xe", "Chủ xe", "Thời gian gửi", "Biển số xe", "Giá gửi"])
        df.to_excel(filename, index=False)

ql_xe = QuanLyXe()

ql_xe.them_xe(Info_Xe("Xe đạp", "Nguyễn Văn A", 10, "22S-1"))
ql_xe.them_xe(Info_Xe("Xe máy", "Nguyễn Văn B", 11, "23B-21"))
ql_xe.them_xe(Info_Xe("Xe điện", "Nguyễn Văn C", 12, "24C-8"))
ql_xe.them_xe(Info_Xe("Ô tô", "Nguyễn Văn C", 13, "25D-46"))

ql_xe.tinh_gia_xe()
xe_tren_20k = ql_xe.xuat_thong_tin_xe_tren_20k()
print("Thông tin những xe có giá gửi trên 20k:")
for xe in xe_tren_20k:
    print(xe)

ql_xe.ghi_du_lieu_vao_excel("Bai3_data_xe.xlsx")