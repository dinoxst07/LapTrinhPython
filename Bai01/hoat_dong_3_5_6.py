#Hoatdong 3
print(f"Hoat dong 3: ")
MUC_LUONG_TOI_THIEU = 5000000

ten = "Dinh Tan Quoc"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2

print("--- THONG TIN SINH VIEN ---")
print(f"Ho va ten: {ten}")
print(f"Diem toan: {diem_toan}")
print(f"Diem van: {diem_van}")
print(f"So luong mon hoc: {so_luong_mon_hoc}")
print(f"Muc luong toi thieu: {MUC_LUONG_TOI_THIEU:,} VND")


#Hoatdong 5
print(f"----------------------------")
print(f"Hoat dong 5.1: ")
a = 17
b = 5
print("a + b =", a + b)     
print("a - b =", a - b)     
print("a * b =", a * b)     
print("a / b =", a / b)     
print("a // b =", a // b)   
print("a % b =", a % b)     
print("a ** b =", a ** b)

print(f"----------------------------")
print(f"Hoat dong 5.2: ")

diem = 6.5
tuoi = 20

kieu_kha = (diem >= 6.5) and (diem < 8.0)
print("Diem dat loai kha:", kieu_kha)  

dieu_kien_tuoi = (tuoi < 18) or (tuoi > 60)
print("Chua du 18 hoac tren 60 tuoi:", dieu_kien_tuoi)  

phu_dinh_tuoi = not dieu_kien_tuoi
print("Phu dinh dieu kien tuoi:", phu_dinh_tuoi)  

print(f"----------------------------")
print(f"Hoat dong 5.3: ")

x = 10
print("Ban dau x =", x)

x += 5   
print("Sau x += 5 :", x) 

x -= 3   
print("Sau x -= 3 :", x)  
print("Sau x *= 2 :", x) 
print("Sau x /= 4 :", x)  
print("Sau x //= 2:", x)  
print("Sau x **= 3:", x)   



danh_sach = [1, 2, 3, "python"]


print("3 co trong danh sach khong ?:", 3 in danh_sach)  

list_a = [1, 2, 3]
list_b = list_a         
list_c = [1, 2, 3]          

print("list_a is list_b:", list_a is list_b) 
print("list_a is list_c:", list_a is list_c) 

print(f"----------------------------")
print(f"Hoat dong 5.4: ")
print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)

print(f"----------------------------")
print(f"Hoat dong 6.1: ")
bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))

print(f"----------------------------")
print(f"Hoat dong 6.2: ")
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0
dtb = (diem_toan + diem_ly + diem_hoa) / 3
la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0
print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)

print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))