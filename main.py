
from models.bankaccount import TaiKhoanNganHang
from models.car import XeOto
from models.employee import NhanVien
from models.rectangular import HinhChuNhat


def start():
    hcn_1 = HinhChuNhat(5, 3)
    hcn_2 = HinhChuNhat(10, 4)
    print(f"Diện tích 1: {hcn_1.tinh_dien_tich()}")
    print(f"Diện tích 2: {hcn_2.tinh_dien_tich()}")
    nv_1 = NhanVien("Nguyen Van A", 15000000)
    nv_2 = NhanVien("Nguyen Van B", 20000000)
    print(f"Tên: {nv_1.ten} | Lương: {nv_1.luong} | Công ty: {nv_1.cong_ty}")
    print(f"Tên: {nv_2.ten} | Lương: {nv_2.luong} | Công ty: {nv_2.cong_ty}")
    tk_1 = TaiKhoanNganHang("Nguyen Van A")
    tk_1.xem_so_du()
    tk_1.nap_tien(500000)
    tk_1.xem_so_du()
    tk_2 = TaiKhoanNganHang("Nguyen Van B", 1000000)
    tk_2.xem_so_du()
    xe_vinfast = XeOto()
    print("Ban đầu:", xe_vinfast.so_banh_xe)
    XeOto.so_banh_xe = 3
    print("Sau khi đổi class attribute:", xe_vinfast.so_banh_xe)
    # Kết quả in ra là 3. Lý do: xe_vinfast không có instance attribute so_banh_xe riêng nên Python tra ngược lên class attribute để lấy giá trị.
    
if __name__ == "__main__":
    start()
