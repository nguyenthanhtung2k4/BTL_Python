# import csv

# class Phong:
#     def __init__(self, so_phong, loai_phong, gia, trang_thai="Trống"):
#         self.so_phong = so_phong
#         self.loai_phong = loai_phong
#         self.gia = gia
#         self.trang_thai = trang_thai

#     def dat_phong(self):
#         if self.trang_thai == "Trống":
#             self.trang_thai = "Đã đặt"
#             print(f"Phòng {self.so_phong} đã được đặt.")
#         else:
#             print(f"Phòng {self.so_phong} đã có người ở.")

#     def tra_phong(self):
#         if self.trang_thai == "Đã đặt":
#             self.trang_thai = "Trống"
#             print(f"Phòng {self.so_phong} đã được trả.")
#         else:
#             print(f"Phòng {self.so_phong} chưa được đặt.")

# def doc_du_lieu_tu_csv(ten_file):
#     """Đọc dữ liệu từ file CSV và tạo danh sách các phòng.

#     Args:
#         ten_file: Tên file CSV.

#     Returns:
#         Danh sách các đối tượng Phong.
#     """
#     danh_sach_phong = []
#     with open(ten_file, 'r', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             phong = Phong(int(row['Số phòng']), row['Loại'], int(row['Giá']), row['Trạng thái'])
#             danh_sach_phong.append(phong)
#     return danh_sach_phong

# def ghi_du_lieu_vao_csv(ten_file, danh_sach_phong):
#     """Ghi danh sách các phòng vào file CSV.

#     Args:
#         ten_file: Tên file CSV.
#         danh_sach_phong: Danh sách các đối tượng Phong.
#     """
#     with open(ten_file, 'w', newline='') as csvfile:
#         fieldnames = ['so_phong', 'loai_phong', 'gia', 'trang_thai']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         for phong in danh_sach_phong:
#             writer.writerow(phong.__dict__)





# file="D:\CODE\DNU_PYTHON\BTL\phòng.csv"
# # Đọc dữ liệu từ file
# danh_sach_phong = doc_du_lieu_tu_csv(file)

# # Tìm kiếm phòng trống
# def tim_phong_trong(danh_sach_phong):
#     for phong in danh_sach_phong:
#         if phong.trang_thai == "Trống":
#             return phong
#     return None

# # Đặt phòng
# phong_can_dat = tim_phong_trong(danh_sach_phong)
# if phong_can_dat:
#     phong_can_dat.dat_phong()
# else:
#     print("Không còn phòng trống!")

# # Ghi lại dữ liệu vào file
# ghi_du_lieu_vao_csv(file, danh_sach_phong)









class Phong:
     # mạc đihnj
     def __init__(self, so_phong, loai_phong, gia, trang_thai):
          self.so_phong = so_phong
          self.loai_phong = loai_phong
          self.gia = gia
          self.trang_thai = trang_thai
#  đặt phòng
     def dat_phong(self):
          if self.trang_thai == "Trống":
               self.trang_thai = "Đã đặt"
               print("Đặt phòng thành công!")
          else:
               print("Phòng đã được đặt!")

     def tra_phong(self):
          if self.trang_thai == "Đã đặt":
               self.trang_thai = "Trống"
               print("Trả phòng thành công!")
          else:
               print("Phòng chưa được đặt!")
     def view_phong(self):
          print( f"Phong: {self.so_phong}\nGia: {self.gia}")

# Tạo một đối tượng phòng
phong1 = Phong(101, "Deluxe", 1000000, "Trống")

# Đặt phòng
print(f'Đặt phòng:')
phong1.dat_phong()
# Xem  phong
print(f'\nXem phòng:')
phong1.view_phong()

b=phong1.gia;b=10;print('gia b  ',b)
print(f'\nXem phòng:')
phong1.view_phong()
# Tra phòng
print(f'\ntra phòng:')
phong1.tra_phong()