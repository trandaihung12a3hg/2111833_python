from phan_so import PhanSo
from danh_sach_phan_so import DanhSachPhanSo

ps1 = PhanSo(-1,2)
ps2 = PhanSo(7,4)
ps3 = PhanSo(2,-3)
ps4 = PhanSo(5,2)

dsps = DanhSachPhanSo()
dsps.them(ps1)
dsps.them(ps2)
dsps.them(ps3)
dsps.them(ps4)

dsps.xuat()
print(dsps.demPSAm())