danh_sach_sach = [
    {"id_sach": "1", "ten_sach": "Truyen Kieu", "gia": 300000, "trang_thai": "Con hang", "so_luong": 10},
    {"id_sach": "2", "ten_sach": "Lao Hac", "gia": 300000, "trang_thai": "Con hang", "so_luong": 10},
    {"id_sach": "3", "ten_sach": "So do", "gia": 300000, "trang_thai": "Con hang", "so_luong": 10},
    {"id_sach": "4", "ten_sach": "Lang Vu Dai", "gia": 300000, "trang_thai": "Con hang", "so_luong": 10},
    {"id_sach": "5", "ten_sach": "Tay Tien", "gia": 300000, "trang_thai": "Con hang", "so_luong": 10},
]
lich_su_doanh_thu = []

def hien_thi_danh_sach_sach():
    print("\n" + "=" * 65)
    print(f"{'Ma sach':<10}{'Ten sach':<15}{'Gia (VND)':<15}{'Trang thai':<15}{'So luong':<10}")
    print("-" * 65)
    for sach in danh_sach_sach:
        print(f"{sach['id_sach']:<10}{sach['ten_sach']:<15}{sach['gia']:>10,}    {sach['trang_thai']:<15}{sach['so_luong']:<10}")
    print("=" * 65)

def tim_sach_theo_ma(id_sach):
    for sach in danh_sach_sach:
        if str(sach["id_sach"]) == str(id_sach):
            return sach
    return None

def them_sach(id_sach, ten_sach, gia, so_luong):
    if tim_sach_theo_ma(id_sach) is not None:
        print(f"-> Ma sach '{id_sach}' da ton tai, khong the them.")
        return
    
    trang_thai = "Con hang" if so_luong > 0 else "Het hang"
    danh_sach_sach.append({
        "id_sach": id_sach, 
        "ten_sach": ten_sach,
        "gia": gia, 
        "trang_thai": trang_thai, 
        "so_luong": so_luong
    })
    print(f"-> Da them sach '{ten_sach}' (Ma: {id_sach}) thanh cong.")

def mua_sach(id_sach, so_luong_mua):
    sach = tim_sach_theo_ma(id_sach)
    if sach is None:
        print(f"-> Khong tim thay sach voi ma '{id_sach}'.")
        return
    
    if so_luong_mua <= 0:
        print("-> So luong mua phai lon hon 0.")
        return
        
    if so_luong_mua > sach["so_luong"]:
        print(f"-> Khong du hang! Trong kho chi con {sach['so_luong']} quyen.")
        return

    thanh_tien = sach["gia"] * so_luong_mua
    ten_sach = sach["ten_sach"]
    
    
    sach["so_luong"] -= so_luong_mua
    if sach["so_luong"] == 0:
        sach["trang_thai"] = "Het hang"

    
    lich_su_doanh_thu.append({
        "id_sach": id_sach, 
        "ten_sach": ten_sach,
        "so_luong_mua": so_luong_mua, 
        "thanh_tien": thanh_tien 
    })
    
    print(f"-> Khach mua thanh cong {so_luong_mua} quyen '{ten_sach}'.")
    print(f"-> Tong tien phai thanh toan: {thanh_tien:,} VND")

def thong_ke_doanh_thu():
    if len(lich_su_doanh_thu) == 0:
        print("-> Chua co giao dich mua sach nao.")
        return
    
    tong_doanh_thu = 0
    print("\n--- LICH SU GIAO DICH ---")
    for gd in lich_su_doanh_thu:
        print(f"Ma: {gd['id_sach']} | Ten: {gd['ten_sach']} | SL: {gd['so_luong_mua']} | Thanh tien: {gd['thanh_tien']:,} VND")
        tong_doanh_thu += gd["thanh_tien"]
    print(f"\n>>> TONG DOANH THU: {tong_doanh_thu:,} VND")

def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            val = int(input(loi_nhac))
            if val < 0:
                print("-> Gia tri phai la so nguyen duong (>= 0). Vui long nhap lai.")
                continue
            return val
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")

def chay_chuong_trinh():
    while True:
        print("\n===== QUAN LY KINH DOANH SACH TAI CUA HANG =====")
        print("1. Hien thi danh sach hien co")
        print("2. Them sach moi")
        print("3. Thanh toan sach")
        print("4. Thong ke doanh thu")
        print("0. Thoat chuong trinh")
        
        lua_chon = input("Nhap lua chon cua ban: ").strip()
        match lua_chon:
            case "1":
                hien_thi_danh_sach_sach()
            case "2":
                id_sach = input("Nhap ma sach moi: ").strip().upper()
                ten_sach = input("Nhap ten sach moi: ").strip().title()
                gia = nhap_so_nguyen("Nhap gia sach/quyen: ")
                so_luong = nhap_so_nguyen("Nhap so luong sach: ")
                them_sach(id_sach, ten_sach, gia, so_luong)
            case "3":
                id_sach = input("Nhap ma sach can mua: ").strip().upper()
                so_luong_mua = nhap_so_nguyen("Nhap so sach da mua: ")
                mua_sach(id_sach, so_luong_mua)
            case "4":
                thong_ke_doanh_thu()
            case "0":
                print("Cam on da su dung chuong trinh. Tam biet!")
                break
            case _:
                print("Lura chon khong hop le, vui long nhap lai.")

if __name__ == "__main__":
    chay_chuong_trinh()